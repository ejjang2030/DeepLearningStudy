# 예제 코드 : wikidocs.net/7030

print('hello world')


icecream = {"탱크보이": 1200, "폴라포": 1200, "빵빠레": 1800, "월드콘": 1500, "메로나": 1000}
new_product = {"팥빙수": 2700, "아맛나": 1000}

icecream.update(new_product)
print(icecream)

keys = ("apple", "pear", "peach")
vals = (300, 250, 400)

dic = dict(zip(keys, vals))
print(dic)

date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_price = dict(zip(date, close_price))
print(close_price)


if True:
    print("1")
    print("2")
else:
    print("3")
print("4")


if True:
    if False:
        print("1")
        print("2")
    else:
        print("3")
else:
    print("4")

print("5")


s = input("입력 : ")
if s == "안녕하세요":
    print(s * 2)

num = int(input("숫자를 입력하세요: "))
if num % 2 == 0:
    print("짝수")
else:
    print("홀수")

