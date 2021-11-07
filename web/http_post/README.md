---
title: "POST Challenge"
level: 2
flag: "FLAG{y0u_ar3_http_p0st_m@ster!}"
writer: "suuhito"
badge: true
---

# post_challenge

## 問題文
HTTP POSTに関する問題を5つ用意しました。すべて解いてFLAGを入手してください！

<https://post.web.wanictf.org/>

## 解法
ヒントのところでおすすめした`curl`, `requests`に加え、`curl`より使いやすいコマンドラインツールである[httpie](https://httpie.io/cli)での解法も書いておこうと思います。
* Challenge 1
```sh
curl -X POST https://post.web.wanictf.org/chal/1 -d 'data=hoge'
```
```python
import requests
print(requests.post("https://post.web.wanictf.org/chal/1", data={"data": "hoge"}).text)
```
```sh
# httpie
http post https://post.web.wanictf.org/chal/1 data=hoge
```

* Challenge 2
  * headerの追加が必要です。
  * `curl`でheaderを追加するには`-H`オプションを利用します。
  * `requests`でheaderを追加するには`headers`パラメータを使用します。
  * `httpie`でheaderを追加するには`=`の代わりに`:`で名前と値を区切ります。
```
curl -X POST https://post.web.wanictf.org/chal/2 -d 'data=hoge' -H 'user-agent: Mozilla/5.0'
```
```python
import requests
print(requests.post("https://post.web.wanictf.org/chal/2", data={"data": "hoge"}, headers={"user-agent": "Mozilla/5.0"}).text)
```
```sh
# httpie
http post https://post.web.wanictf.org/chal/2 data=hoge user-agent:Mozilla/5.0
```

* Challenge 3
  * 名前でブラケット表記`[]`を使うことでネストしたデータを送信することができます。
  * JSON形式でも可能(詳しくはChallenge 4を参照)
```
curl -X POST https://post.web.wanictf.org/chal/3 -d 'data[hoge]=fuga'
curl -X POST https://post.web.wanictf.org/chal/3 -H "Content-Type: application/json" -d '{"data": {"hoge": "fuga"}}'
```
```python
import requests
print(requests.post("https://post.web.wanictf.org/chal/3", data={"data[hoge]": "fuga"}).text)
print(requests.post("https://post.web.wanictf.org/chal/3", json={"data": {"hoge": "fuga"}}).text)
```
```sh
# httpie
# httpieはデフォルトでJSONで送信している、form形式で送信するためには-fを付ける
http -f post https://post.web.wanictf.org/chal/3 "data[hoge]=fuga"
http post https://post.web.wanictf.org/chal/3 data:='{"hoge": "fuga"}'
```

* Challenge 4
  * 文字列ではなく数字や`null`などを送信したい場合は[JSON](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/JSON)形式で送信します。
  * `curl`でJSON形式で送るためには、まず`Content-Type`ヘッダに`application/json`を指定してサーバに送信したデータがJSONであることを教える必要があります。
  * `requests`を使用する場合はJSONで送信するための`json`パラメータが存在し、それを利用するとヘッダは自動的に追加されます。
  * `httpie`は実はデフォルトでJSON形式で送信しています。文字列以外を送信するためには`:=`で名前と値を区切ります。
```
curl -X POST https://post.web.wanictf.org/chal/4 -H "Content-Type: application/json" -d '{"hoge": 1, "fuga": null}'
```
```python
import requests
print(requests.post("https://post.web.wanictf.org/chal/4", json={"hoge": 1, "fuga": None}).text)
```
```sh
# httpie
http post https://post.web.wanictf.org/chal/4 hoge:=1 fuga:=null
```

* Challenge 5
  * カレントディレクトリに`wani.png`([https://post.web.wanictf.org/](https://post.web.wanictf.org/)で表示されるワニの画像)を保存しているという前提です。
  * `curl`で`multipart/form-data`形式でファイルを送るためには、`-d`オプションの代わりに`-F`を使用します。
  * `requests`で`multipart/form-data`形式でファイルを送るためには、`files`パラメータを利用します。
  * `httpie`で`multipart/form-data`形式でファイルを送るためには、`-f`オプションを付けたうえで`@`で名前と値を区切ります。
```
curl -X POST https://post.web.wanictf.org/chal/5 -F data=@wani.png
```
```python
import requests
print(requests.post("https://post.web.wanictf.org/chal/5", files={"data": open("wani.png", "rb")}).text)
```
```sh
# httpie
http -f post https://post.web.wanictf.org/chal/5 data@wani.png
```
