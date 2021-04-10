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
#list = ["hello.py", "ex01.py", "intro.hwp"]
import re
#for i in list:
#    print(i.split(".")[0])
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
'''
# 162
for i in range(1998, 2051, 4):
    print(i)

# 164
for i in range(99, -1, -1):
    print(i)
    '''
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
'''
# 166 167
for i in range(1, 10, 2):
    # print(f"3x{i}={3 * i}")
    # print(3, "x", i, "=", 3 * i)
    print(f"3x{i}={i * 3}")

# 168
a = 0
for i in range(1, 11):
    a += i
print(a)

# 168
print(sum(range(1, 11)))

# 168
print("합 :", sum([i for i in range(1, 11)]))

# 169
a = 0
for i in range(1, 11):
    if i % 2 == 1:
        a += i
print("합 :", a)

# 169
print("합 :", sum([i for i in range(1, 11) if i % 2 == 1]))

# 170
a = 1
for i in range(1, 11):
    a *= i
print(a)
'''

# print(list(map(lambda a, i: a * i, 1, i for i in range(1, 11))))

# 171
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(price_list[i])

# 172
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(i, price_list[i])
for i, v in enumerate(price_list):
    print(i, v)

# 173
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(3 - i, price_list[i])

'''
my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(len(my_list) - 2):
    print((my_list[i] + my_list[i + 1] + my_list[i + 2]) / 3)
'''
print()

low_prices = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for i in range(5):
    volatility.append(high_prices[i] - low_prices[i])
print(volatility)


def print_coin():
    print("비트코인")


print_coin()


def print_coins():
    for i in range(100):
        print_coin()


print_coins()


def print_with_smile(string):
    print(string + ":D")

print_with_smile("hello")


# 217
def print_upper_price(price):
    price += price * 0.3
    print(price)


# 218
def print_sum(a, b):
    print(a + b)


# 220
def print_max(a, b, c):
    if a < b:
        if b < c:
            print(c)
        else:
            print(b)
    else:
        if b < c:
            print(c)
        else:
            print(a)


print_max(1, 2, 3)


# 221
def print_reverse(string):
    print(string[::-1])


print_reverse("python")


# 222
def print_score(lst):
    print(sum(lst) / len(lst))

print_score([1, 2, 3])


# 223
def print_even(lst):
    for v in lst:
        if v % 2 == 0:
            print(v)


print_even([1, 3, 2, 10, 12, 11, 15])


# 235
def convert_int(string):
    print(int(string.replace(',', '')))


convert_int("1,234,567")


# 236
def 함수(num):
    return num + 4


a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)


# 237
def 함수(num):
    return num + 4

c = 함수(함수(함수(10)))
print(c)


# 238
def 함수1(num):
    return num + 4

def 함수2(num):
    num = num + 2
    return 함수1(num)

c = 함수1(10)
print(c)


# 240
def 함수0(num):
    return num * 2

def 함수1(num):
    return 함수0(num + 2)

def 함수2(num):
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)


# 292
with open("C:/Users/Thinkodia/Desktop/매수종목2.txt", "w") as f:
    l = ["005930 삼성전자", "005380 현대차", "035420 NAVER"]
    for v in l:
        data = f"{v}\n"
        f.write(data)


# 293
import csv
with open("C:/Users/Thinkodia/Desktop/매수종목.csv", mode="wt", encoding='cp949', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["종목명", "종목코드", "PER"])
    writer.writerow(["삼성전자", "005930", 15.59])
    writer.writerow(["NAVER", "035420", 55.82])


# 294
with open("C:/Users/Thinkodia/Desktop/매수종목1.txt", mode='rt', encoding='utf-8') as f:
    codes = []
    for line in f.readlines():
        code = line.strip()
        codes.append(code)
    print(codes)


# 295
with open("C:/Users/Thinkodia/Desktop/매수종목2.txt", mode='rt') as f:
    d = dict()
    for line in f.readlines():
        line = line.strip()
        line = line.split(' ')
        d[line[0]] = line[1]
    print(d)


# 296
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except ValueError:
        print(0)


# 297
per = ["10.31", "", "8.00"]
new = []

for i in per:
    try:
        v = float(i)
    except ValueError:
        v = 0
    new.append(v)

print(new)


# 298
try:
    b = 3 / 0
except ZeroDivisionError:
    print("0으로 나누면 안되요")


data = [1, 2, 3]
try:
    for i in range(5):
        print(data[i])
except IndexError as e:
    print(e, ": End of Index")

for i in range(5):
    try:
        print(data[i])
    except IndexError as e:
        print(e)


# 300
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except ValueError:
        print(0)
    else:
        print("예외 없음")
    finally:
        print("반복문 처리 완료")

