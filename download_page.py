import requests

uql = "https://online.metro-cc.ru/virtual/sad_i_ogorod-5696?in_stock=1"


headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15"
}
req = requests.get(uql, headers=headers)
src = req.text

with open("pages/index.html", "w") as f:
    f.write(src)
