import json
import pandas as pd

# DataFrame => 二維陣列 (is composed of multiplee pyseries)
grade_python = pd.Series([70,60,50,40],index=["c201","c202","c203","c204"])
grade_php = pd.Series([100,50,80,70],index=["c201","c202","c203","c204"])
grade_html = pd.Series([50,70,60,90],index=["c201","c202","c203","c204"])
grade_ALL = pd.DataFrame({"Python":grade_python, "PHP":grade_php, "HTML":grade_html})

print(grade_ALL)
print("----------------------------")
print(grade_ALL.head(2)) # 頭
print(grade_ALL.tail(2)) # 尾
print("===========================================")

# 敘述性統計資料，(平均、標準差......)
print(grade_ALL.describe())
print("--------------------------------------------")
# transpos 轉置矩陣
print(grade_ALL.T)
print(grade_ALL.T.describe())
print("===========================================")

#slice 切片
print(grade_ALL[['Python','PHP']]) # 欄 (直切)
print("-------------------")
# loc
print(grade_ALL.loc[['c202','c204'],['Python','PHP']])# 列 (橫切)
print("-------------------")
# iloc 
print(grade_ALL.iloc[[1]])
print(grade_ALL.iloc[[1,3],[0,1]])
print("============================")

print(grade_ALL)

print("----------------------------")
# drop 刪除
tmp = grade_ALL.drop('c203',axis=0)
print(tmp)
print("============================")

# 判斷式 (過濾條件)
print(grade_ALL[grade_ALL['Python']<60])

print("============================")

f = open('C:/ALL/NKUST/VS_Code/程式設計/下學期/上課/JSON/data_Ubike.json','r',encoding='utf-8')
data = json.load(f)
f.close()
tmp = data["retVal"]
Ubk_DF = pd.DataFrame(tmp)
print(Ubk_DF)

Ubk_DFok = Ubk_DF[['area_code','district_tw','parking_spaces','name_tw']]
print(Ubk_DFok)

print(Ubk_DFok.loc[4128,'area_code']) # selection by label
print(Ubk_DFok.iloc[4128,0]) # selection by postion
print("-----------")
print(Ubk_DFok['area_code'].value_counts())
print("--------------")
ntp = Ubk_DFok[Ubk_DFok["area_code"]=="05"]
print(ntp)
# groupby
print(ntp.groupby('district_tw').count())

result = ntp.groupby('district_tw').count()['name_tw']
print(result.sort_values())
