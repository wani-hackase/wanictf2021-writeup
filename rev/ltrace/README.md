---
title: ltrace
level: 1
flag: FLAG{c4n_y0u_7r4c3_dyn4m1c_l1br4ry_c4ll5?}
writer: hi120ki, Laika
---

# ltrace

## 問題文

この問題はltraceで解ける...ってコト!?

```
$ sudo apt-get install -y ltrace
$ ltrace --help
```

ヒント : オプションをよく確認しよう

## 解法

2つターミナルを用意します。

ターミナル1で配布されたバイナリを実行します。

```
$ sudo chmod +x ltrace
$ ./ltrace
Input flag :
```

するとこのように文字列の入力待ちとなります。そしてターミナル1では何もせず、ターミナル1で実行しているバイナリのPIDをターミナル2上で調べます。

```
$ ps -C ltrace
    PID TTY          TIME CMD
   9787 pts/0    00:00:00 ltrace
```

ここではPIDが`9787`であるとわかったのでltraceでPIDを指定してこのバイナリがどんな共有ライブラリの関数を呼び出すか調べます。

ターミナル2で引き続き

```
$ sudo ltrace -p 9787
```

を実行してターミナル1で適当な文字を打ち込みエンターを押します。

```
$ ./ltrace
Input flag : a
Incorrect
```

するとターミナル2ではフラグ文字列の比較を行う`strcmp`関数が呼ばれていたことが確認できます。

```
$ sudo ltrace -p 9787
strcmp("a", "FLAG{c4n_y0u_7r4c3_dyn4m1c_l1br4"...)                 = 27
puts("Incorrect")                                                  = 10
+++ exited (status 1) +++
```

ltraceはこのように`strcmp`や`puts`などの共有ライブラリで提供される関数をトレースすることができます。

ここでは適当に入力した`"a"`とフラグ文字列`"FLAG{c4n_y0u_7r4c3_dyn4m1c_l1br4"...`を比較していますが、文字が途中で切れているためフラグは取得できていません。

よってここでltraceの`-s`オプション(specify the maximum string size to print.)を指定してフラグ文字列を全て出力させます。

同様にバイナリを実行し、PIDを取得してltraceを実行すると

```
$ sudo ltrace -p 9929 -s 50
strcmp("a", "FLAG{c4n_y0u_7r4c3_dyn4m1c_l1br4ry_c4ll5?}")          = 27
puts("Incorrect")                                                  = 10
+++ exited (status 1) +++
```

このようにフラグ文字列が全て出てきました。
