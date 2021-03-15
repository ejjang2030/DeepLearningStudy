import urllib.request
url = "http://api.aoikujira.com/ip/ini"

mem = urllib.request.urlopen(url).read()
print(mem.decode("utf-8"))