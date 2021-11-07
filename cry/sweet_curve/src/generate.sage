from random import randint

from Crypto.Util.number import bytes_to_long, getPrime, long_to_bytes
from sage.all import *

p = getPrime(512)
flag = b"FLAG{7h1s_curv3_alw@ys_r3m1nd5_me_0f_pucca}"
description = """
# Given:
# - An elliptic curve: y**2 = x**3 - x + 1 (mod p)
# - Two points: P(x_P, y_P) and Q(x_Q, y_Q)

# Find the point P+Q
# The flag is the x value of P+Q
# Don't forget to convert it into a string!
""".strip()

# y^2 = x^3 - x + 1 (mod p)
E = EllipticCurve(Zmod(p), [-1, 1])

x_R = mod(bytes_to_long(flag), p)
y_R = (x_R ^ 3 - x_R + 1).sqrt(all=True)[0]
R = E(x_R, y_R)

x_P = mod(randint(2, p - 1), p)
y_P = (x_P ^ 3 - x_P + 1).sqrt(all=True)[0]
P = E(x_P, y_P)

Q = R - P

recovered_flag = (P + Q).xy()[0]
recovered_flag = int(recovered_flag)
if flag == long_to_bytes(recovered_flag):
    print(description)

    print(f"{p = :#x}")
    print(f"x_P = {int(x_P):#x}")
    print(f"y_P = {int(y_P):#x}")
    print(f"x_Q = {int(Q.xy()[0]):#x}")
    print(f"y_Q = {int(Q.xy()[1]):#x}")
