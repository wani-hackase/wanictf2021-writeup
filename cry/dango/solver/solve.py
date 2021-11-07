from functools import reduce


def XOR(*X):
    xor = lambda A, B: bytes(x ^ y for x, y in zip(A, B))
    return reduce(xor, X)


with open("../file/output.txt") as f:
    ciphertext = bytes.fromhex(f.readline().split(" : ")[-1])
    A = bytes.fromhex(f.readline().split(" : ")[-1])
    B = bytes.fromhex(f.readline().split(" : ")[-1])
    C = bytes.fromhex(f.readline().split(" : ")[-1])


key1 = XOR(A, B, C)
key0 = XOR(B, key1)
print(XOR(ciphertext, key0))
