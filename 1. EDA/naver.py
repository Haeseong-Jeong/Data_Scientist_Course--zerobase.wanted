import pandas as pd
import requests
from bs4 import BeautifulSoup


url = "https://finance.naver.com/marketindex/"
response = requests.get(url) # requests.get(url) / requests.post(url) 나중에 비교해보자.

soup = BeautifulSoup(response.text,"html.parser")

exchangeList = soup.select("#exchangeList > li") # 셀렉트는 리스트값을 반환함


exchange_dates = []
baseUrl = "https://finance.naver.com/"

for item in exchangeList:
    data = {
        "title" : item.select_one(".h_lst").text,
        "exchange" : item.select_one(".value").text,
        "change" : item.select_one(".change").text,
        "updown" : item.select_one(".head_info.point_dn > .blind").text,
        "link" : baseUrl + item.select_one("a").get("href")
    }
    exchange_dates.append(data)

#print(exchange_dates)


df = pd.DataFrame(exchange_dates)
df.to_excel("./naverfinance.xlsx", encoding = "utf-8")