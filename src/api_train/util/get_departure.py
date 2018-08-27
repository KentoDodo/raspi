import os, json
from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient

from setting import DB_HOST, DB_PORT


client = MongoClient(DB_HOST, DB_PORT)

db = client["train"]


def get_html(url):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    _html = r.text

    return _html


html = get_html("http://ekikara.jp/newdata/ekijikoku/1301051/up1_12102021.htm")
# html = get_html("http://ekikara.jp/newdata/ekijikoku/1301051/up1_12102021_sat.htm")
# html = get_html("http://ekikara.jp/newdata/ekijikoku/1301051/up1_12102021_holi.htm")
# html = get_html("http://ekikara.jp/newdata/ekijikoku/1301051/down1_12102021.htm")
soup = BeautifulSoup(html, "html.parser")


_info = soup.select("td.lowBg04")[1].get_text().split("\xa0")
info = {
    "station": _info[0],
    "line": _info[1],
    "direction": _info[2],
    "week": _info[3]
}
collection = db["departure"]
_info = collection.find_one(info)
if _info:
    info = _info
else:
    collection.insert_one(info)
print(info)

departure_id = info["_id"]

collection = db["departure/%s" % departure_id]
collection.remove()

go_to_prefixs = []
_go_to_prefixs_text = soup.select("td.tdWid02")[0].find_parent().find_all("td")[2].find("span")
go_to_prefixs_texts = _go_to_prefixs_text.get_text().replace(" ", "").replace("\r\n", "").replace("\xa0", "").split(",")
go_to_prefixs += [go_to_prefixs_text.split("…") for go_to_prefixs_text in go_to_prefixs_texts]
go_to_prefixs = dict(go_to_prefixs)
print(go_to_prefixs)

trains = []
trs = soup.select(".lowBg01 > table > tbody > tr")
for tr in trs:
    tds = tr.find_all("td")
    if len(tds) < 2:
        continue
    hour = tds[0].select("span.textBold")[0].get_text()
    _trains = tds[1].select("table td")
    for _train in _trains[0:-1:2]:
        go_to = _train.select("span.s")[0].get_text()
        minute = _train.select("span.textBold > a")[0].get_text()
        train = {
            "go_to": go_to_prefixs[go_to],
            "hour": int(hour),
            "minute": int(minute)
        }
        trains.append(train)
        result = collection.insert_one(train)
        print(train)
