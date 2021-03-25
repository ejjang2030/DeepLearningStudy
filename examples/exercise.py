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

fruit = ["사과", "귤", "수박"]
for v in fruit:
    print(v)
for v in fruit:
    print("#####")


for v in ["A", "B", "C"]:
    print("출력:", v)


for v in ["A", "B", "C"]:
    b = v.lower()
    print("변환:", b)
    
변수 = "A"
b = 변수.lower()
print("변환:", b)
변수 = "B"
b = 변수.lower()
print("변환:", b)
변수 = "C"
b = 변수.lower()
print("변환:", b)


for n in range(10, 40, 10):
    print(n)

for n in range(1, 4):
    print(n * 10)

for n in range(1, 4):
    print(n * 10)
    print("-------")

for i in range(4):
    print("-------")


# 141
리스트 = [100, 200, 300]
for i in 리스트:
    print(i + 10)

# 142
리스트 = ["김밥", "라면", "튀김"]
for i in 리스트:
    print("오늘의 메뉴:", i)

# 143
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for i in 리스트:
    print(len(i))

# 144
리스트 = ["dog", "cat", "parrot"]
for i in 리스트:
    print(i, len(i))

# 145
리스트 = ["dog", "cat", "parrot"]
for i in 리스트:
    print(i[0])

# 146
리스트 = [1, 2, 3]
for i in 리스트:
    print(3, "x", i)

# 147
리스트 = [1, 2, 3]
for i in 리스트:
    print(3, "x", i, "=", 3 * i)


# 154
l = ["I", "study", "python", "language", "!"]
for i in l:
    if len(i) >= 3:
        print(i)

# 155
l = ["A", "b", "c", "D"]
for i in l:
    if i.isupper():
        print(i)


# 156
l = ["A", "b", "c", "D"]
for i in l:
    if i.islower():
        print(i)

for i in l:
    if not i.isupper():
        print(i)


l = ["dog", "cat", "parrot"]
for i in l:
    print(i.replace(i[0], i[0].upper()))
    # print(i[0].upper() + i[1:])
    # print(i.title())
    # print(i.capitalize())
'''
# 158
list = ["hello.py", "ex01.py", "intro.hwp"]
import re
for i in list:
    print(i.split(".")[0])
'''

list = ["intra.h", "intra.c", "define.h", "run.py"]
for i in list:
    if i.find(".h") > 0:
        print(i)
# find() : ".h" 문자열이 있으면 그 문자열이 시작되는 인덱스를 반환하고 없으면 -1을 반환

# 160
for i in list:
    if i.find(".h") > 0 or i.find(".c") > 0:
        print(i)


# 161
for i in range(100):
    print(i, end=" ")
'''

# 162
for i in range(1998, 2051, 4):
    print(i)

# 164
for i in range(99, -1, -1):
    print(i)
"""
for i in range(100):
    print(99 - i)
"""
'''
# 165
for i in range(10):
    print('0.' + str(i))
'''
'''
# 165
for i in range(10):
    print('0.' + str(i))
    print(i / 10)
    print("%.1f" % (i * 0.1))
'''

# 166
for i in range(1, 10):
    print(f"3x{i}={3 * i}")
    # print(3, "x", i, "=", 3 * i)


