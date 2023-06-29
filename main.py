import csv

import requests
from bs4 import BeautifulSoup

from download_page import parse

ENCODING = "utf-8"

parse()

with open("pages/index.html") as file:
    src = file.read()

with open("data/products.csv", "w", encoding=ENCODING) as file:
    writer = csv.writer(file)
    writer.writerow((
        "id товара",
        "наименование",
        "ссылка на товар",
        "регулровая цена",
        "промо цена",
        "бренд"
    ))

soup = BeautifulSoup(src, "lxml")

all_data = soup.find_all(class_="subcategory-or-type__products-item")
for item in all_data:
    prod_id = item.get("data-sku")
    prod_href = "https://online.metro-cc.ru" + item.find(
        class_="product-card-photo__link"
        ).get("href")
    prod_name = item.find(class_="product-card-photo__link").get("title")
    try:
        prod_price_full = item.find(
            class_="product-price__sum-rubles"
            ).find_next(class_="product-price__sum-rubles").text
        prod_price_dicount = item.find(class_="product-price__sum-rubles").text
    except Exception:
        prod_price_full = item.find(class_="product-price__sum-rubles").text

    req = requests.get(url=prod_href)
    src = req.text
    soup_detail = BeautifulSoup(src, "lxml")
    prod_brand = soup_detail.find(
        class_="product-attributes__list-item-link reset-link active-blue-text"
        ).text.strip()

    with open("data/products.csv", "a", encoding=ENCODING) as file:
        writer = csv.writer(file)
        writer.writerow((
            prod_id,
            prod_name,
            prod_href,
            prod_price_full,
            prod_price_dicount,
            prod_brand
        ))
