import base64

import requests


def cry_flagservice(host):
    if "http" not in host:
        host = "https://" + host

    try:
        res = requests.get(host, timeout=3)
        res.raise_for_status()
    except Exception:
        return 2

    try:
        data = {"username": "laik"}
        s = requests.Session()
        s.post(host + "/login", data=data, timeout=3)

        # Modify the token
        token = s.cookies["token"]
        token = base64.b64decode(token)
        iv, rest = token[:16], token[16:]
        iv = list(iv)
        iv[10] ^= ord("f") ^ ord("t")
        iv[11] ^= ord("a") ^ ord("r")
        iv[12] ^= ord("l") ^ ord("u")
        iv[13] ^= ord("s") ^ ord("e")
        iv[14] ^= ord("e") ^ ord(" ")
        iv = bytes(iv)
        forged_token = base64.b64encode(iv + rest)

        cookies = {"token": forged_token.decode()}
        res = requests.get(host, cookies=cookies, timeout=3)
        if "FLAG{Fl1p_Flip_Fl1p_Flip_Fl1p____voila!!}" in res.text:
            return 0
        else:
            return 1

    except Exception:
        return 1


if __name__ == "__main__":
    print(cry_flagservice("http://localhost"))
