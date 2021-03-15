import matplotlib.pyplot as plt
import pandas as pd

# Pandas로 CSV 파일 읽어 들이기
tbl = pd.read_csv("blood_presure.csv", index_col=2)

# 그래프 그리기 시작
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)


# 서브 플롯 전용 - 지정한 레이블을 임의의 색으로 칠하기
def scatter(lbl, color):
    b = tbl.loc[lbl]
    ax.scatter(b["systolic_bp"], b["diastolic_bp"], c=color, label=lbl)


scatter("hypotension", "blue")
scatter("normal", "green")
scatter("prehypertension", "yellow")
scatter("stage 1 hypertension", "orange")
scatter("stage 2 hypertension", "pink")
scatter("hypertension crisis", "red")
scatter("none", "gray")

ax.legend()
plt.savefig("blood-presure-test.png")
# plt.show()
print("png file has been created!")