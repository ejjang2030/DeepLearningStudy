import urllib.request
import urllib.parse

api = "https://search.naver.com/search.naver"

values = {
    "where": "nexearch",
    "sm": "top_hty",
    "fbm": "1",
    "ie": "utf8",
    "query": "클럽하우스"
}

params = urllib.parse.urlencode(values)

url = api + "?" + params
print(url)

data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)