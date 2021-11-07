---
title: fox
level: 1
flag: FLAG{R1ng_d1n9_ding_d1ng_ding3ring3ding?__Wa_p@_pa_p@_pa_p@_pow?__or_konko-n?}
writer: Laika
---

# fox

## 問題文
What does the fox say?🦊
## 解法
逆の操作を実装する。8ビットずつ復号するとよい。
実は、`int.from_bytes` や `Crypto.Util.number.bytes_to_long` と同等なので、これらを利用しても良い。
