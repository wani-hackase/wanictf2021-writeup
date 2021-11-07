---
title: Flag Service
level: 5
flag: FLAG{Fl1p_Flip_Fl1p_Flip_Fl1p____voila!!}
badge: true
writer: Laika
---

# Flag Service

## 問題文
🚩🤵

https://service.crypto.wanictf.org


## 解法
CookieにAES-CBCで暗号化されたトークンが保存されている。
トークンはAES-CBCのIVと認証情報から構成されており、全体がBase64でエンコードされている。
認証情報は
`{"admin": false, "username": "Laika"}`
のようになっており、このトークンを参照してadminか否かを判定している。すなわち、このadminの値をtrueにできれば良い。

ここで
- 暗号化がAES-CBCである。
- tokenにAES-CBCで利用するIVが含まれており、復号時に利用している。
ことに注目すると、IVを変更することで、暗号化された認証情報の先頭16バイトは任意の値に改ざん可能である。
先頭16バイトは `{"admin": false,` であるから、false → trueに改ざんし、認証を突破できる。
