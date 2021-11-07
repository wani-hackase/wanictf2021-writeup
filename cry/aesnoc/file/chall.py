import os

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.strxor import strxor

from secret import flag


class AESNOC:
    def __init__(self, key: bytes, iv: bytes):
        self.iv = iv
        self.key = key
        self.block_size = AES.block_size

    def encrypt(self, plaintext: bytes):
        cipher = AES.new(self.key, AES.MODE_ECB)
        plaintext = pad(plaintext, self.block_size)
        P = [
            plaintext[i : i + self.block_size]
            for i in range(0, len(plaintext), self.block_size)
        ]
        C = []

        P_prev = self.iv
        for p in P:
            c = cipher.encrypt(p)
            C.append(strxor(c, P_prev))
            P_prev = p

        return b"".join(C)


def main():
    key = os.urandom(16)
    iv = os.urandom(16)
    cipher = AESNOC(key, iv)

    assert len(flag) == 49
    assert flag.startswith(b"FLAG{")
    assert flag.endswith(b"}")

    iv = iv.hex()
    print(f"{iv = }")
    while True:
        print("1. Get encrypted flag")
        print("2. Encrypt")
        choice = int(input("> "))
        if choice == 1:
            encrypted_flag = cipher.encrypt(flag).hex()
            print(f"{encrypted_flag = }")
        elif choice == 2:
            plaintext = input("Plaintext [hex] > ")
            plaintext = bytes.fromhex(plaintext)
            ciphertext = cipher.encrypt(plaintext).hex()
            print(f"{ciphertext = }")
        else:
            print("Bye")
            break


if __name__ == "__main__":
    main()
