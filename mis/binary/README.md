---
title: binary
level: 1
flag: FLAG{binary-is-essential-for-communication}
writer: saru
---

# binary
## 問題文

+ 無線通信問題1問目です。
+ 文字も所詮1と0の集合です。
+ sample.pyを参考に復号器を作ってみてください。
+ binary.csvは1列目が時刻、2列目がON-OFFの信号を表しています。
+ ASK、ASK over the airと進む中で無線通信の面白さが伝われば．．．と思っています。
+ 「binary」はWaniCTF 2021-springとほぼ同じ問題なのでハードルが高いと感じる人は、「WaniCTF 2021-spring binary writeup」でぐぐりつつ解いてみてください。

## 解法

### はじめに

フラグの文字列をバイナリにして2進数にしているだけなので逆に1bitずつつめてchar型に変換しながら出力するだけです。
ただ、前回と違ってcsvて一列目がタイムスタンプになってしまっているので2列目を見る必要があります。

```
fp = open("./binary.csv", "r")

data = []
fp.readline()
while True:
    vals = fp.readline()
    if vals == "":
        break

    vals = vals.split(",")
    data.append(int(vals[1]))

c = 0
for i in range(len(data)):
    c = (c << 1) | data[i]
    if i % 8 == 7:
        print(chr(c), end="")
        c = 0

print("")
```
