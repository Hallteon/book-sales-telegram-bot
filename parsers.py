import re

import requests
from bs4 import BeautifulSoup

headers = {"accept": "*/*",
           "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ("
                         "KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"}


async def scraper_book24():
    data = {}

    url = "https://book24.ru/sales/"

    req = requests.get(url, headers=headers)
    src = req.text
    soup = BeautifulSoup(src, "lxml")

    blocks = soup.find_all("div", class_="sales-tabs-item__body")

    sales = []
    descriptions = []
    before = []
    links = []

    for block in blocks:
        try:
            sale = block.find("a", class_="sales-tabs-item__title-link")
            descript = block.find("div", class_="sales-tabs-item__desc")
            bef = block.find_all("span", class_="info-list__text")[-1]
            link = sale.get("href")

            sales.append(sale.text.lstrip())
            descriptions.append(descript.text.lstrip())
            before.append(bef.text.lstrip())
            links.append(link.lstrip())

        except:
            continue

    data["sales"] = sales
    data["descriptions"] = descriptions
    data["before"] = before
    data["links"] = links

    return data


async def scraper_chitay_gorod():
    data = {}

    url = "https://www.chitai-gorod.ru/actions/"

    req = requests.get(url, headers=headers)
    src = req.text

    soup = BeautifulSoup(src, "lxml")

    blocks = soup.find_all("div", class_="action-card")

    sales = []
    descriptions = []
    before = []
    links = []

    for block in blocks:
        try:
            sale = block.find("a", class_="action-card__title")
            descript = block.find("div", class_="action-card__description")
            bef = block.find("div", class_="action-card__date").find("span", class_="color_red")
            link = sale.get("href")

            sales.append(sale.text)
            descriptions.append(descript.text)
            before.append(bef.text)
            links.append(link)
        except:
            continue

    data["sales"] = sales
    data["descriptions"] = descriptions
    data["before"] = before
    data["links"] = links

    return data

