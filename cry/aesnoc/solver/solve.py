import re

from Crypto.Util.Padding import unpad

from pwn import *


def XOR(*array):
    array = list(array)
    X = array.pop()
    for Y in array:
        X = bytes(x ^ y for x, y in zip(X, Y))
    return X


_r = remote("localhost", 50000)


def parse(name):
    value = re.findall(f"{name} = '(.*)'", _r.recvline().decode())[0]
    value = bytes.fromhex(value)
    return value


def get_encrypted_flag():
    _r.sendlineafter(b"> ", b"1")
    encrypted_flag = parse("encrypted_flag")
    return encrypted_flag


def encrypt(plaintext: bytes):
    _r.sendlineafter(b"> ", b"2")
    _r.sendlineafter(b"> ", plaintext.hex().encode())
    ciphertext = parse("ciphertext")
    return ciphertext


iv = parse("iv")
encrypted_flag = get_encrypted_flag()
C = [encrypted_flag[i : i + 16] for i in range(0, len(encrypted_flag), 16)]
P = [b"" for _ in range(len(C))]
P[3] = b"}\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f"


for i in range(3, 0, -1):
    P[i - 1] = XOR(encrypt(P[i]), C[i], iv)

flag = unpad(b"".join(P), 16)
print(flag)
