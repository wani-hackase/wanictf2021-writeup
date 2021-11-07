---
title: nc
level: 1
badge: true
flag: FLAG{the-1st-step-to-pwn-is-netcatting}
writer: saru
---

# nc

## 問題文

```
nc nc.pwn.wanictf.org 9001
```

### ヒント

+ netcat (nc)と呼ばれるコマンドを使うだけです。
+ つないだら何も出力されなくてもLinuxコマンドを打ってenterを入力してみましょう。
+ [Linuxの基本的なコマンド集](https://rat.cis.k.hosei.ac.jp/article/linux/command.html)
+ pwnの問題ではシェルが取れたときに何も出力されないので分かり辛いですが、とりあえず`ls`とか実行してみるとシェルが取れてたりすることがあります。

### 使用ツール例
+ [netcat (nc)](https://github.com/wani-hackase/memo-setup-pwn-utils#netcat)

## 解法

ncで接続して`cat flag.txt`を入力するとflagの中身が見れます。
これは多くの人が解いていたので大丈夫かと思います。
