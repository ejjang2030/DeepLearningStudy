import random


# Blood Presure(혈압)을 계산해서 레이블을 리턴하는 함수
def calculate_blood_presure(systolic_bp, diastolic_bp):
    if systolic_bp > diastolic_bp:
        if 120 > systolic_bp >= 90:
            if 80 > diastolic_bp >= 60:
                return "normal"  # 정상혈압
            else:
                return "none"
        elif 90 > systolic_bp >= 60:
            if 60 > diastolic_bp >= 40:
                return "hypotension"  # 저혈압
            else:
                return "none"
        elif 140 > systolic_bp >= 120:
            if 90 > diastolic_bp >= 80:
                return "prehypertension"  # 고혈압 전단계
            else:
                return "none"
        elif 160 > systolic_bp >= 140:
            if 100 > diastolic_bp >= 90:
                return "stage 1 hypertension"  # 1기 고혈압
            else:
                return "none"
        elif 180 > systolic_bp >= 160:
            if 110 > diastolic_bp >= 100:
                return "stage 2 hypertension"  # 2기 고혈압
            else:
                return "none"
        elif 230 > systolic_bp >= 180:
            if 150 > diastolic_bp >= 110:
                return "hypertension crisis"  # 고혈압 위기
            else:
                return "none"
        else:
            return "none"
    else:
        return "none"


# 출력 파일 준비하기
fp = open("blood_presure.csv", "w", encoding="utf-8")
fp.write("systolic_bp,diastolic_bp,label\r\n")

# 무작위로 데이터 생성하기
cnt = {"normal": 0, "hypotension": 0, "prehypertension": 0, "stage 1 hypertension": 0, "stage 2 hypertension": 0, "hypertension crisis": 0, "none": 0}
for i in range(100000):
    systolic_bp = random.randint(60, 230)
    diastolic_bp = random.randint(40, 150)
    label = calculate_blood_presure(systolic_bp, diastolic_bp)
    # if label == "none":
       # continue
    cnt[label] += 1
    fp.write("{0},{1},{2}\r\n".format(systolic_bp, diastolic_bp, label))
fp.close()
print("file created! :", cnt)
