import base64
import json
import os

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class AESCBC:
    def __init__(self):
        self.key = os.urandom(16)

    def encrypt(self, data: str):
        cipher = AES.new(self.key, AES.MODE_CBC)

        iv = cipher.iv
        data = json.dumps(data)

        ciphertext = cipher.encrypt(pad(data.encode(), AES.block_size))

        token = base64.b64encode(iv + ciphertext)
        return token

    def decrypt(self, token: bytes):
        token = base64.b64decode(token)

        iv, ciphertext = token[: AES.block_size], token[AES.block_size :]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)

        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

        data = json.loads(plaintext)
        return data
