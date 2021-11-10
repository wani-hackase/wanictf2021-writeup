---
title: AES-NOC
level: 4
flag: FLAG{Wh47_h4pp3n$_1f_y0u_kn0w_the_la5t_bl0ck___?}
badge: true
writer: Laika
---

# AES-NOC

## 問題文
AES-CBCか...って、あれ？

`nc aesnoc.crypto.wanictf.org 50000`

## 解法

> ライトテーマの方は[こちら](https://github.com/wani-hackase/wanictf2021-writeup/blob/main/cry/aesnoc/README_light.md)

AES-ECBをベースに独自実装したAES-NOCなるもので暗号化されている。
これはAES-CBCのXORをとる箇所が変わったものと考えると良い。

平文を16バイトごとのブロックに区切った配列を  <img src="https://latex.codecogs.com/svg.image?%5Ccolor%7Bwhite%7DP_i%20%28i%20%3D%200%2C%201%2C%202%2C%203%29">、暗号文を同様に区切った配列を <img src="https://latex.codecogs.com/svg.image?%5Ccolor%7Bwhite%7DC_i%20%28i%20%3D%200%2C%201%2C%202%2C%203%29"> とする。
またassert文より、末尾が`}`かつflagの長さが49であるので、paddingを考慮すると、平文の最後のブロック <img src="https://latex.codecogs.com/svg.image?%5Ccolor%7Bwhite%7DP_3"> は
`b"}\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f"`
となることが分かる。

ここで <img src="https://latex.codecogs.com/svg.image?%5Ccolor%7Bwhite%7DP_%7Bi-1%7D%20%3D%20\text{encrypt}%28P_i%29%20%5Coplus%20C_i"> であることから、<img src="https://latex.codecogs.com/svg.image?%5Ccolor%7Bwhite%7D\text{encrypt}(P_i)"> を接続先で計算し、<img src="https://latex.codecogs.com/svg.image?%5Ccolor%7Bwhite%7DC_i"> とXORを取ることで、<img src="https://latex.codecogs.com/svg.image?%5Ccolor%7Bwhite%7DP_3">から順に平文を求めてflagを得ることができる。
