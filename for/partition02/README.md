---
title: partition02
level: 4
flag: FLAG{you_found_flag_in_FLAGs}
writer: takushooo
---

# partition02

## 問題文

FLAG01とFLAG02にflag画像を分割して入れておきました．

> 添付のファイルは"partition01"と同じものです．

## 解法
partition01の続き．

partition01ではtestdiskでパーティション名の一覧を確認できた．

partition01でFLAGとなったパーティション名以外に`FLAG01`と`FLAG02`というパーティション名が確認できる．これが問題文のパーティション名である．

partition02では，パーティションをマウントするための情報として，パーティションのスタート位置の情報が必要となる．
testdiskの情報から，FLAG01のスタート位置は`2099200`，FLAG02のスタート位置は`2623488`とわかる．

offset指定してtmpにマウント場合，以下のようなコマンドになる．
```
sudo mount -o loop,offset=`expr [first sector] \* 512` FIND_FLAG.img tmp/
```

これをFLAG01とFLAG02にそれぞれやるとそれぞれからflag01，flag02が手に入る．
flag01を開くと途中で切れてるので，flag02と合わせる．
```
cat flag0* > output.png
```