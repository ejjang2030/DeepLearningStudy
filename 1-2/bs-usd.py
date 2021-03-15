from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.naver.com/marketindex/?tabSel=worldExchange#tab_section"
res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser")

price = soup.select_one("div.head_info > span.value").string
print("usd/krw =", price)
