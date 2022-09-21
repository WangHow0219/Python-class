import json

f = open('data_Ubike.json','r',encoding='utf-8')

# Json(key:value) ==> keyList & valueList
data = json.load(f)
f.close()
tmp = data["retVal"]

allValue = []
for i in tmp:
    allKey = []
    tmpValue = []
    for key,value in i.items():
        allKey.append(key)
        tmpValue.append(value)
    allValue.append(tmpValue)

# print(len(tmp))
# print(len(allKey))
# print(len(allValue))


# # list generator
# allKey2 = [key for key ,value in tmp[0].items()]
# # print(len(allKey2))

# allValue2 = []
# for i in tmp:
#     tmpValue = [ value for key,value in i.items()]
#     allValue2.append(tmpValue)
# # print(len(allValue2))


# keyList & valueList ==> .csv
#keyList
header = ",".join(allKey)
# print(header)

#valueList
Data = ""
for i in allValue:
    tmp1 = ",".join([ str(k) for k in i]) + "\n"
    Data = Data + tmp1
# print(Data)

o = open('data_Ubike.csv','w',encoding='utf-8')
o.write(header)
o.write(Data)
o.close()
