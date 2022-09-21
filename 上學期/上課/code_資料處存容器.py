dict1 = {"侯先生":900,"張小姐":800,"林小弟":30,"王小妹":30}
print(dict1["侯先生"])
print(dict1["侯小弟"])
# get // key 不存在時，不會產生錯誤。回傳None
print(dict1.get("侯小弟"))
print(dict1.get("侯小弟","不在字典中"))

# 範例 (天氣)
dict2 = {"春":"暖","夏":"熱","秋":"涼","冬":"冷"}
name = input("輸入季節(春夏秋冬):")
feeling = str(dict2.get(name))
if feeling == None:
    print("沒有"+name+"季節")
else:
    print(name+"天氣為:"+ feeling)

# 刪除字典
# 1.指定特定元素 //語法:del 字典名稱[key]
lang = {"好":"Good","哈囉":"Hello"}
del lang["哈囉"]

# 2.刪除字典所有元素 // 字典名稱.clear()
lang.clear()

# 3.刪除整個字典(不存在) // del 字典名稱
del lang

# 合併字典 // update
lang1 = {"您好":"Hello"}
lang2 = {"早安":"Good  Morning"}
lang1.update(lang2)
print(lang1)

#複製
#指向同一個字典物件
lang3={"您好":"Hello"}
lang4=lang3
lang4["您好"]="Hi"

# copy()指向不同字典物件
lang3={"您好":"Hello"}
lang4=lang3.copy()
lang4["您好"]="Hi"

# keys & values
dict3 = {"春":"暖","夏":"熱","秋":"涼","冬":"冷"}
keys1 = dict3.keys()
print(keys1)
print(keys1[0])

keys2 = list(keys1)
print(keys2[0])

values1 = dict3.values()
print(values1)
print(values1[0])

values2 = list(values1)
print(values2[2])

#items()
lang1 = {"早安":"Good Morning","您好":"Hello"}
for ch, en in lang1.items():
    print("中文為",ch,"英文為",en)

#set 集合 // {}或set
s = {1,2,3,4}

s = set(('a',1,'b',2))

s = set(['apple',1,'banana',2])

s = set({"早安":"Good Morning","您好":"Hello"})

#add and remove
s = set("NKUST")
s.add("z")
s.remove("N")

# set 運算
a = set("NKUST")
b = set("KMU")
print(a|b)#聯集
print(a&b)#交集
print(a-b)#差集
print(a^b)#互斥或

a = set("123456")
b = set("123")
print(a|b)#聯集
print(a&b)#交集
print(a-b)#差集
print(a^b)#互斥或

# 集合的比較
s1 = set("NKUST")
s2 = set("NKUSTs")
print(s1<s2)#真子集合
print(s1<=s2)#子集合
print(s1>=s2)#超集合
print(s1>s2)#真超集合