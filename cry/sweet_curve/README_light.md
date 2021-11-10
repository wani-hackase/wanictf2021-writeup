---
title: Sweet curve
level: 3
flag: FLAG{7h1s_curv3_alw@ys_r3m1nd5_me_0f_pucca}
writer: Laika
---

# Sweet curve

## 問題文
🥠🍩🍪



## 解法

> ダークテーマの方は[こちら](https://github.com/wani-hackase/wanictf2021-writeup/blob/main/cry/sweet_curve/README.md)

有限体上の楕円曲線 <img src="https://latex.codecogs.com/svg.image?%5ccolor{black}%20E%3A%20y%5E2%20%3D%20x%5E3%20-%20x%20%2B%201%20%5Cpmod%20p"> と、2点 <img src="https://latex.codecogs.com/svg.image?%5ccolor{black}P%28x_P%2C%20y_P%29%2C%20Q%28x_Q%2C%20y_Q%29"/> が与えられる。これに対して <img src="https://latex.codecogs.com/svg.image?%5ccolor{black}P%2BQ"> を計算すると、そのx座標がflagとなっている。


###  解法1
楕円曲線上の2点の加算は、<img src="https://latex.codecogs.com/svg.image?%5ccolor{black}R%20=%20P%2BQ"> とすると

<img src="https://latex.codecogs.com/svg.image?%5ccolor{black}%5Cleft%5C%7B%0A%5Cbegin%7Baligned%7D%0Ax_R%20%26%3D%20%5Calpha%5E2%20-%20x_P%20-%20x_Q%20%5C%5C%20%5Cnonumber%0Ay_R%20%26%3D%20-%5Calpha%20x_R%20-%20%5Cbeta%20%5Cnonumber%0A%5Cend%7Baligned%7D%0A%5Cright.">
で与えられる。ただし、

<img src="https://latex.codecogs.com/svg.image?%5ccolor{black}%5Cbegin%7Baligned%7D%0A%5Calpha%20%26%3D%20%5Cfrac%7By_Q-y_P%7D%7Bx_Q-x_P%7D%20%5C%5C%0A%5Cbeta%20%26%3D%20%5Cfrac%7By_Px_Q%20-%20y_Qx_P%7D%7Bx_Q-x_P%7D%0A%5Cend%7Baligned%7D">
とする。


[solve.py](solver/solve.py)
```python
p = 0x89A4E2C7F834F5FBC6F2A314E373E3723DE7DF6283C5D97CBCA509C61E02965B7EF96EFCE1D827BFDFA7F21D22803558BB549F9EA15DFE9F47D3976648C55FEB


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        a = (self.y - other.y) * pow(self.x - other.x, -1, p) % p
        b = (self.y * other.x - other.y * self.x) * pow(self.x - other.x, -1, p) % p
        x_R = (a * a - self.x - other.x) % p
        y_R = (-a * x_R - b) % p
        return Point(x_R, y_R)


x_P = 0x1E1CBA0E07C61CF88E9F23B9859093C33C26CF83BCFB6FE24D7559CD0EA86FB2F144AE643AC5EDF6F04EF065DC7C2C18D88AE02843592D5E611029FEFC0FECE
y_P = 0x198420B30A4330F82380326895D0AC06A1859BC49D45CD4B08021B857D23D515163B9151FBAF7AE5F816D485D129D3B1C4630D1FB45C6790AF551428A5C85667
x_Q = 0x7E32EDFD7BEFD8DF93D7B738D6A1C95E1CFD56B3A6CCC4A62E4E0AE9059B4903E71FCCBE07D8D45C762B4A3ED5C9D1A2505043D033E58ADB72191259B81BC47D
y_Q = 0x46016C676585FEAF048FFF9D5CBB45DBD598C6C4C81694E0881BF110B57012F0BAC6EAF7376FEE015C8CECBA1FC92206CA346F7D72EE1D60F820091C85FA76B3


P = Point(x_P, y_P)
Q = Point(x_Q, y_Q)
R = P + Q
flag = R.x
flag = bytes.fromhex(f"{flag:x}")
print(flag)
```


### 解法2

[SageMath](https://www.sagemath.org/)などのツールを利用することで、簡単に楕円曲線の演算を行える。

CryptoではSageMathを利用する場面が多い。高機能ゆえに使い慣れるまでは持て余してしまうので、とにかく使いまくるのがおすすめ。

[solve.sage](solver/solve.sage)
```sage
from sage.all import EllipticCurve, FiniteField

p = 0x89A4E2C7F834F5FBC6F2A314E373E3723DE7DF6283C5D97CBCA509C61E02965B7EF96EFCE1D827BFDFA7F21D22803558BB549F9EA15DFE9F47D3976648C55FEB
x_P = 0x1E1CBA0E07C61CF88E9F23B9859093C33C26CF83BCFB6FE24D7559CD0EA86FB2F144AE643AC5EDF6F04EF065DC7C2C18D88AE02843592D5E611029FEFC0FECE
y_P = 0x198420B30A4330F82380326895D0AC06A1859BC49D45CD4B08021B857D23D515163B9151FBAF7AE5F816D485D129D3B1C4630D1FB45C6790AF551428A5C85667
x_Q = 0x7E32EDFD7BEFD8DF93D7B738D6A1C95E1CFD56B3A6CCC4A62E4E0AE9059B4903E71FCCBE07D8D45C762B4A3ED5C9D1A2505043D033E58ADB72191259B81BC47D
y_Q = 0x46016C676585FEAF048FFF9D5CBB45DBD598C6C4C81694E0881BF110B57012F0BAC6EAF7376FEE015C8CECBA1FC92206CA346F7D72EE1D60F820091C85FA76B3

E = EllipticCurve(FiniteField(p), [-1, 1])
P = E(x_P, y_P)
Q = E(x_Q, y_Q)

R = P + Q

flag = int(R.xy()[0])
flag = bytes.fromhex(f"{flag:x}")
print(flag)
```
