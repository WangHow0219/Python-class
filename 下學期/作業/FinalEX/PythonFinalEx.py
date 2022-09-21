"""
一、從 政府公開資訊平台 抓取最新資料
"""
import requests
import json
import pandas as pd
"""
get Json from Internet
"""
data = {'lang':'tw','type':'2'}
req = requests.get("https://od.cdc.gov.tw/eic/Age_County_Gender_day_19Cov.json",params = data)
if req.status_code == 200:
    data_Str = req.content.decode('utf-8')
    # str => json
    tmp = json.loads(data_Str)
    f = open("data.json",'wb')
    # json => str
    data_Json = json.dumps(tmp,indent=4,ensure_ascii=False).encode('utf8')
    f.write(data_Json)

    f.close()
"""
二、資料處裡
Data Processing
"""
# 把資料表存進變數 Data_DF
Data_DF = pd.DataFrame(tmp)
# print(Data_DF)

# 製作資料總表
All_DF = Data_DF[['發病日','縣市','性別','年齡層','確定病例數','是否為境外移入']]
All_DF[['確定病例數']] = All_DF[['確定病例數']].astype(int)
# print(All_DF)

# 刪除 是 '境外移入' 的資料
abroad = All_DF[ All_DF['是否為境外移入'] == '是' ].index
All_DF.drop(abroad, inplace=True)
print("------台灣境內所有確診資料表------")
print(All_DF)

# 各縣市 每日確診數
Tw_DF = All_DF[['發病日','縣市','確定病例數']]
print("------各縣市 每日確診數------")
print(Tw_DF)

# 全台 每日確診數
TwDay_DF = Tw_DF.groupby('發病日').sum()[['確定病例數']]
print("------全台 每日確診數------")
print(TwDay_DF)

# 各縣市 累計確診數
County_count = Tw_DF.groupby('縣市').sum()[['確定病例數']]
County_count = County_count.sort_values(['確定病例數'],ascending=False)
print("------各縣市 累計確診數------")
print(County_count)
County_count.to_csv("County_count.csv", header=True)

# 六都 每日確診數
cityName = ['台北市','新北市','桃園市','台中市','台南市','高雄市']
cityID = ['TPE','NTP','TYN','TXG','TNA','KSH']
notCityID = ['notTPE','notNTP','notTYN','notTXG','notTNA','notKSH']
for k in range(6):
    notCityID[k] = Tw_DF[ Tw_DF['縣市'] != cityName[k] ].index
    cityID[k] = Tw_DF.drop(notCityID[k])
    cityID[k] = cityID[k].groupby('發病日').sum()[['確定病例數']]
    print("======="+cityName[k]+"每日確診數=======")
    print(cityID[k])

# 所有確診者 性別比例
gender = All_DF[['性別','確定病例數']]
gender = gender.groupby('性別').sum()[['確定病例數']]
gender.reset_index(inplace = True)
gender.loc[gender.性別=="F",'性別']="女性"
gender.loc[gender.性別=="M",'性別']="男性"
gender.loc[gender.性別=="U",'性別']="未知"
gender.loc[gender.性別=="X",'性別']="第三性別"
gender.set_index('性別',inplace=True)
print("------所有確診者 性別比例------")
print(gender)
gender.to_csv("Gender.csv", header=True)

# 所有確診者 年齡分布
Age = All_DF[['年齡層','確定病例數']]
Age = Age.groupby('年齡層').sum()[['確定病例數']]
# print("------Before------")
# print(Age)
Age.reset_index(inplace = True)
Age.loc[1] = [ '5-9',Age.loc[[13],['確定病例數']].values ]
Age.loc[0] = [ '0-4',Age.loc[[0,1,4,7,10],['確定病例數']].sum().values ]
Age.drop(Age.index[[4,7,10,13]],inplace=True)
Age.set_index('年齡層',inplace=True)
print("------所有確診者 年齡分布------")
print(Age)
Age.to_csv("Age.csv", header=True)