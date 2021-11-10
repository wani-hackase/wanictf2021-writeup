---
title: dango
level: 2
flag: FLAG{dango_sankyodai_dango__-ooo-}
writer: Laika
---

# dango

## 問題文
🍡

## 解法

> ダークテーマの方は[こちら](https://github.com/wani-hackase/wanictf2021-writeup/blob/main/cry/dango/README.md)

各パラメータは以下のようになっている。

<img src="https://latex.codecogs.com/svg.image?\color{black}\left\{%5Cbegin%7Baligned%7D%0A%5Ctext%7Bciphertext%7D%20%26%3D%20%5Ctext%7Bflag%7D%20%5Coplus%20K_0%20%5C%5C%0AA%20%26%3D%20K_0%20%5Coplus%20K_1%20%5Coplus%20K_2%20%5C%5C%0AB%20%26%3D%20K_0%20%5Coplus%20K_1%20%5C%5C%0AC%20%26%3D%20K_1%20%5Coplus%20K_2%0A%5Cend%7Baligned%7D\right.">

ここで、
<img src="https://latex.codecogs.com/svg.image?\color{black}X%20\oplus%20X%20%3D%200">
であることを利用すると、

<img src="https://latex.codecogs.com/svg.image?\color{black}%5Cbegin%7Baligned%7D%0A%5Ctext%7Bciphertext%7D%20%5Coplus%20A%20%5Coplus%20C%20%0A%20%20%26%3D%20%28%5Ctext%7Bflag%7D%20%5Coplus%20K_0%29%20%5Coplus%20%28K_0%20%5Coplus%20K_1%20%5Coplus%20K_2%29%20%5Coplus%20%28K_1%20%5Coplus%20K_2%29%20%5C%5C%0A%20%20%26%3D%20%5Ctext%7Bflag%7D%20%5Coplus%20%28K_0%20%5Coplus%20K_0%29%20%5Coplus%20%28K_1%20%5Coplus%20K_1%29%20%5Coplus%20%28K_2%20%5Coplus%20K_2%29%20%5C%5C%0A%20%20%26%3D%20%5Ctext%7Bflag%7D%20%0A%5Cend%7Baligned%7D">
となり、flagが得られる。
