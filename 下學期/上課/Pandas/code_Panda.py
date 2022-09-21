import pandas as pd
import json

# Series => 一維陣列
data1 = pd.Series([70,80,90,100],index=["國","英","數","社"])
# data1 = pd.Series({"國":70, "英":80, "數":90, "社":100})
print(data1["英":"社"])
print(data1[::-1])
print(data1[["英","社"]])

data2 = pd.Series([10,20,30,40,50])
print(data2[2:5])
print(data2[::-2])
print(data2[[1,4]])

# DataFrame => 二維陣列 (is composed of multiplee pyseries)
grade_python = pd.Series([70,60,50,40],index=["c201","c202","c203","c204"])
grade_php = pd.Series([100,90,80,70],index=["c201","c202","c203","c204"])
grade_html = pd.Series([80,70,60,90],index=["c201","c202","c203","c204"])
grade_ALL = pd.DataFrame({"Python":grade_python, "PHP":grade_php, "HTML":grade_html})
print(grade_ALL)
print(grade_ALL.index) # 列名稱
print(grade_ALL.values) # 值
print(grade_ALL.columns) # 欄位名稱
print("=========================================================")

# json --> Panda.DataFrame
f = open('C:/ALL/NKUST/VS_Code/程式設計/下學期/上課/JSON/data_Ubike.json','r',encoding='utf-8')
# str --> dict
data = json.load(f)
f.close()

tmp = data["retVal"]

# dict --> Panda.DataFrame
Ubk_DF = pd.DataFrame(tmp)
# print(Ubk_DF)
# print(Ubk_DF.index)
# print(Ubk_DF.columns)

# DataFrame --> .csv
# Ubk_DF.to_csv("data_Ubike.csv", index=False ,header=True)
# Ubk_DF.to_excel("data_Ubike.xls", index=False)

print("=========================================================")


