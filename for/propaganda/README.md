---
title: propaganda
level: 1
flag: FLAG{Stand_tall_We_are_Valorant_We_are_fighters!}
writer: takushooo
---

# propaganda

## 問題文

超人気ゲームをみんなでプレイしよう！

## 解法

これは，[サブリミナル広告](https://ja.wikipedia.org/wiki/%E3%82%B5%E3%83%96%E3%83%AA%E3%83%9F%E3%83%8A%E3%83%AB%E5%8A%B9%E6%9E%9C)と呼ばれる禁止されている宣伝手法がある．
この問題でも，FLAGが記入されているフレームがあるので，ffmpegでフレームを切り出すか，スロー再生で文字の書かれたフレームを探してFLAGを手に入れる．

ffmpegなら以下のようなコマンドになる．
```
ffmpeg -i flag.mp4 ./output/%03d.jpg
```