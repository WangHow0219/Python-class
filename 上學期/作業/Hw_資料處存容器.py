#Hw_六都PM輸出
dict1 = {
    "高雄市":9, "新北市":5,
    "台北市":4, "台南市":8,
    "台中市":6, "桃園市":7
}
city = input("輸入要查詢的六都名稱:")
check = dict1.get(city)
if check == None:
    print("六都中沒有 "+str(city)+" 城市!")
else:
    print(str(city) + " 今天的 PM2.5 值為 : "
          + str(dict1[city]))

#Hw_生肖個性輸出顯示
dict2 = {
    "鼠":"親切和藹",
    "牛":"保守努力",
    "虎":"熱情大膽",
    "兔":"溫柔仁慈"
}
for animal, Traits in dict2.items():
    print("屬",animal,"特質為 :",Traits)

#Hw_排序
numb_box = []
for i in range(1, 11):
    numb_box.append(int(input("請輸入共 10 個數字")))
print("你的數列 :", numb_box)
numb_box.sort(reverse=True)
print("最大的 3 個數字為 : ",end="")
for i in range(0, 3):
    print(numb_box[i],end=" ")
print(" ")
print("最小的 3 個數字為 : ",end="")
for i in range(9, 6, -1):
    print(numb_box[i],end=" ")
