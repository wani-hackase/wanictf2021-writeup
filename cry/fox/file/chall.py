flag = b"FAKE{REDACTED}"


def bytes_to_int(B: bytes):
    X = 0
    for b in B:
        X <<= 8
        X += b
    return X


print(bytes_to_int(flag))
