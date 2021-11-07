---
title: breakRAID
level: 5
flag: FLAG{ra1dr4idxxxx}
writer: takushooo
---

# breakRAID

## 問題文

HDDが1台壊れてしまったみたいです．

## 解法

配布ファイルを`file`コマンドで調べると以下のような出力が得られる．
```
disks/disk00: data
disks/disk01: Linux Software RAID version 1.2 (1) UUID=2dfa6967:99457c4e:cce8f079:7a80f14d name=ishioka:0 level=5 disks=3
disks/disk02: Linux Software RAID version 1.2 (1) UUID=2dfa6967:99457c4e:cce8f079:7a80f14d name=ishioka:0 level=5 disks=3
```
disk01とdisk02の出力から，「3本のHDDで構築されたRAID5」の一部であることがわかる．
問題文から，disk00もその一部であると考えられる．

RAID5は，データを複数のハードディスクに分散して格納するもので，パリティデータを書き込むことによる耐障害性に特徴がある．
RAID5の必要HDD本数は3本以上で，1本の故障までなら耐障害性がある．

つまり，今回の問題は故障していない2本のHDDから故障した1本のHDDのデータを再構築すればよい．
RAID5ではパリティの生成にXOR演算が使用される．

今回は全部で3本なので，単純にdisk01とdisk02をxorしてmdadmでマウントする．
まず，[xor-files](https://www.nirsoft.net/utils/xorfiles.html)や，以下のようなスクリプトを使ってdisk01とdisk02をxor演算する．

``` xor.py
with open('disk01', 'rb') as f:
    d1 = f.read()

with open('disk02', 'rb') as g:
    d2 = g.read()

with open('disk00', 'wb') as h:
    h.write(bytes(x^y for x, y in zip(d1, d2)))
```

disk00が作成できたら，以下のような手順でマウントする．
loopbackデバイスには空いているやつを適当に使う．
``` mount.sh
#!/bin/sh

sudo losetup /dev/loop50 disk00
sudo losetup /dev/loop51 disk01
sudo losetup /dev/loop52 disk02

sudo mdadm --create /dev/md0 --level=5 --raid-devices=3 /dev/loop50 /dev/loop51 /dev/loop52
mkdir tmp
sudo mount /dev/md0 tmp
```
出てきた画像をファイル名の番号順に並べると，FLAGになる．
