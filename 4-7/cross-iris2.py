import pandas as pd
from sklearn import svm, metrics, model_selection
import random
import re

# 붓꽃의 CSV 데이터 읽어 들이기
csv = pd.read_csv("iris.csv")

# 리스트를 훈련 전용 데이터와 테스트 전용 데이터로 분할하기
data = csv[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
label = csv["Name"]

# 크로스 밸리데이션하기
clf = svm.SVC()
scores = model_selection.cross_val_score(clf, data, label, cv=5)
print("각각의 정답률 =", scores)
print("평균 정답률 =", scores.mean())
