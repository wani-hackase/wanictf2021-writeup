---
title: poly
level: 3
flag: FLAG{thisismpng3}
writer: takushooo
---

# sonic

## 問題文

お前...pngか...？

> FLAGの中身はすべて小文字です．

## 解法

この問題の難関は音声が聞き取ることだった人もいたかもしれないですが，今回の解法には含まれません．

### 解法1
steganography問題でpng画像が出てきたときに結構多用するのが[zsteg](https://github.com/zed-0xff/zsteg)というツール．

zstegをつかうことでpngやbmpに埋め込まれたデータを検出することができる．

```
zsteg flag.png
zsteg -E 'extradata:0' flag.png > extract.mp3
```

### 解法2
配布したpng画像は，一見ただのpngですが拡張子を変えてvlc等で再生することでmp3として再生できます．

元ネタはこの[ツイート](https://twitter.com/David3141593/status/1371974874856587268)
```
cp flag.png flag.mp3
vlc flag.mp3
```