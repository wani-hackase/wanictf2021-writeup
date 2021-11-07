import re

from pwn import *


def XOR(*array):
    array = list(array)
    X = array.pop()
    for Y in array:
        X = bytes(x ^ y for x, y in zip(X, Y))
    return X


def parse(name: str, _r):
    value = re.findall(f"{name} = '(.*)'", _r.recvline().decode())[0]
    value = bytes.fromhex(value)
    return value


def get_encrypted_flag(_r):
    _r.sendlineafter(b"> ", b"1")
    encrypted_flag = parse("encrypted_flag", _r)
    return encrypted_flag


def encrypt(plaintext: bytes, _r):
    _r.sendlineafter(b"> ", b"2")
    _r.sendlineafter(b"> ", plaintext.hex().encode())
    ciphertext = parse("ciphertext", _r)
    return ciphertext


def check_cry_aesnoc(host):
    try:
        _r = remote(host, 50000)
    except Exception:
        return 2

    try:
        iv = parse("iv", _r)
        encrypted_flag = get_encrypted_flag(_r)
        C = [encrypted_flag[i : i + 16] for i in range(0, len(encrypted_flag), 16)]
        P = [b"" for _ in range(len(C))]
        P[3] = b"}\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f"

        for i in range(3, 0, -1):
            P[i - 1] = XOR(encrypt(P[i], _r), C[i], iv)

        flag = b"".join(P)
        if b"FLAG{Wh47_h4pp3n$_1f_3ncryp710n_w3r3_d3cryp710n?}" in flag:
            return 0
        else:
            return 1
    except Exception:
        return 1


if __name__ == "__main__":
    print(check_cry_aesnoc("localhost"))
