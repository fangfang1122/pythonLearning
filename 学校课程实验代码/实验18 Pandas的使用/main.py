import pandas as pd
import numpy as np
import random
from matplotlib import pyplot as plt

# （一）	从18.student_score.csv文件中读取同学的成绩册，处理好缺失值。
df = pd.read_csv('18.student_score.csv')
df = df.fillna(method="backfill")  # 处理缺失值
print(df)

# Series 类型创建
a = pd.Series([9, 8, 7, 6])
print(a)
# DataFrame类型创建
d= pd.DataFrame(np.arange(10).reshape(2,5))
print(d)

# 将实验报告成绩从ABCD转换成百分制，统计出实验成绩。A为90分，B为75分，C为60分，D为40分。
def m(x):  # 将ABCD转化为对应的分数
    if x == "A":
        return 90
    if x == "B":
        return 75
    if x == "C":
        return 60
    if x == "D":
        return 40


df["实验成绩百分制"] = df.实验报告成绩.map(m)
print(df)

# （三）按照平时成绩20%，实验成绩30%，期末成绩50%的比例计算综合成绩，形成新的综合成绩列。
df["综合成绩"] = df["期末成绩"] * 0.5 + df["平时成绩"] * 0.2 + df["实验成绩百分制"] * 0.3
print(df)

# （四）统计全班综合成绩[90,100],[80,89],[70,79],[60-69],[0,59]各段成绩的人数，并画饼图。
y = pd.cut(df['综合成绩'], bins=[0, 60, 70, 80, 90, 100],
           labels=['0-59', '60-69', '70-79', '80-89', '90-100'])  # 分区间
a = y.value_counts()  # 统计区间人数
print(a)
plt.rcParams['font.sans-serif'] = ['SimHei']
a.plot(kind='pie', title='学生成绩区间统计图')
plt.show()

# （五）将完整的成绩保存到score.csv文件中，打开excel检查输出是否正确。
# df.to_excel(excel_writer="score.xlsx", index=False, encoding='utf-8')
# pd.read_excel("score.xlsx")
save = pd.DataFrame(df)
save.to_csv('score.csv', index=False, encoding="utf_8_sig")
