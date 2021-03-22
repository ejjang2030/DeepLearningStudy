import re
'''
post_num = input("우편번호: ")
post_num_list = ['강북구', '강북구', '강북구', '도봉구', '도봉구', '도봉구', '노원구', '노원구', '노원구']
print(post_num_list[int(post_num[2])])
'''
'''
if int(id_num[7:][0]) % 2 == 1:
    print("남자")
elif int(id_num[7:][0]) % 2 == 0:
    print("여자")
if 0 <= int(id_num[7:][2:4]) <= 8:
    print("서울 입니다.")
elif 8 < int(id_num[7:][2:4]):
    print("서울이 아닙니다.")
id_num = input("주민등록번호: ")
id_num = id_num.replace("-", '')
id_num_list = []
for v in id_num:
    id_num_list.append(int(v))
nums = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
total = 0
for i in range(12):
    total += (int(id_num_list[i]) * nums[i])
validationCheckRest = total % 11
isValidNumber = 11 - validationCheckRest
if int(id_num[-1]) == isValidNumber:
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")
'''

import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# 종가? = (시가 + 변동폭) = (시가 + (최고가 - 최저가)) > 최고가
closing_price = int(btc["closing_price"])
opening_price = int(btc["opening_price"])
min_price = int(btc["min_price"])
max_price = int(btc["max_price"])
if opening_price + (max_price - min_price) > max_price:
    print("상승장")
else:
    print("하락장")

