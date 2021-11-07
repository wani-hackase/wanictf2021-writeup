# fmt: off
flag = b"FLAG{R1ng_d1n9_ding_d1ng_ding3ring3ding?__Wa_p@_pa_p@_pa_p@_pow?__or_konko-n?}"
# fmt: on


def bytes_to_int(B: bytes):
    X = 0
    for b in B:
        X <<= 8
        X += b
    return X


print(bytes_to_int(flag))
