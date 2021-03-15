from bs4 import BeautifulSoup
import urllib.request as req

url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

dongju_intro1 = soup.select_one('#mw-content-text > div.mw-parser-output > table:nth-child(2) > tbody > tr td')
# nth-child가 안될때
# dongju_intro1 = soup.select_one('#mw-content-text > div.mw-parser-output > table:nth-of-type(2) > tbody > tr td')
print(dongju_intro1.text)

a_list = soup.select("#mw-content-text > div > ul > li a")
b_list = soup.select("#mw-content-text > div > ul > li > ul > li a")

for a in a_list:
    name = a.string
    print("-", name)
    if name == "하늘과 바람과 별과 시":
        for b in b_list:
            s = b.string
            print("  -", s)


