with open("output.txt") as f:
    X = int(f.read())


def int_to_bytes(X):
    B = []
    while X > 0:
        B = [X & 0xFF] + B
        X >>= 8

    return bytes(B)


print(int_to_bytes(X))
