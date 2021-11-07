---
title: partition01
level: 2
flag: FLAG{GPT03}
writer: takushooo
---

# partition01

## 問題文

新しくUSBを買ったのでたくさんパーティションを作ってみました！

## 解法
GPT (Globally Unique Identifier (GUID) Partition Table)と呼ばれるHDDのパーティション管理の仕組みを使ってフォーマットしたイメージファイルを解析する問題．

現在ほぼすべてのディスクが今回のGPTか，MBR (Master Boot Record)と呼ばれる仕組みを採用している．

GPTはMBRに比べて新しい規格で，古いOSバージョンではサポートできないが，MBRディスクの2TBの容量制限がないというメリットがある．
また，パーティションの数も無制限である．

[testdisk](https://www.cgsecurity.org/wiki/TestDisk_JP)による解析で，パーティション名を見ていく．
以下のコマンドを打って，
```
testdisk partition.img
```
`Proceed` &rarr; `EFI GPT` &rarr; `Analyse` &rarr; `Quick Search`と進んでいくと，パーティション名が見れる．

FLAGは第3パーティションのパーティション名．

### 別解
この問題はもちろんstringsでも解ける．
やってほしい解き方ではないので，少しのダミーとヒントを入れておいた．

ただのいやがらせです．