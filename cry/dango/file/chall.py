import secrets
from functools import reduce

flag = b"FAKE{REDACTED}"
key = [secrets.token_bytes(len(flag)) for _ in range(3)]


def XOR(*X):
    xor = lambda A, B: bytes(x ^ y for x, y in zip(A, B))
    return reduce(xor, X)


ciphertext = XOR(flag, key[0])
A = XOR(key[0], key[1], key[2])
B = XOR(key[0], key[1])
C = XOR(key[1], key[2])

print(f"ciphertext : {ciphertext.hex()}")
print(f"A : {A.hex()}")
print(f"B : {B.hex()}")
print(f"C : {C.hex()}")
