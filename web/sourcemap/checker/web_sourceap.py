import requests
import urllib.parse as urlparse
from bs4 import BeautifulSoup

# SSL Warning
# import urllib3
# urllib3.disable_warnings()


def web_sourceap(host):
    if "http" not in host:
        host = "https://" + host

    # connect check
    try:
        res = requests.get(urlparse.urljoin(host, "index.html"), timeout=3)
        res.raise_for_status()
    except Exception:
        return 2

    # check solve
    try:
        res = requests.get(urlparse.urljoin(host, "index.html"), timeout=3)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, features="lxml")
        sources = soup.findAll("script", {"src": True})
        for source in sources:
            res = requests.get(
                urlparse.urljoin(host, source["src"] + ".map"), timeout=3
            )
            res.raise_for_status()
            if "FLAG" in res.text:
                return 0
        return 1
    except Exception:
        return 1


if __name__ == "__main__":
    print(web_sourceap("http://localhost"))
