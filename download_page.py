import requests

uql = "https://online.metro-cc.ru/virtual/sad_i_ogorod-5696?in_stock=1"

req = requests.get(uql)
src = req.text


def parse():
    with open("pages/index.html", "w") as f:
        f.write(src)
