#取代字母
while True:
    TEXT = input('檢測的字串(end 結束)')
    if TEXT == 'end':
        print('檢測結束')
        break
    else:
        oldText = input('搜尋目標字元')
        oldCount = TEXT.count(oldText)
        print(f"字元{oldText}出現次數為:{oldCount}")

        newTextAndCount = input('取代該字元 & 取代次數')
        newText = newTextAndCount[0]        
        newCount = int(newTextAndCount[1])

        final = TEXT.replace(oldText,newText,newCount)
        print(f"取代後字串為 : {final}")

#排序
numb_box = []
for i in range(1, 11):
    numb_box.append(int(input("請輸入共 10 個數字")))
print("你的數列 :", numb_box)
numb_box.sort()
print("最大的3個數字為 : ",end="")
print(numb_box[9], numb_box[8], numb_box[7])
print("最小的3個數字為 : ",end="")
print(numb_box[0], numb_box[1], numb_box[2])

#猜顏色
ans = ['red', 'blue', 'red', 'green']
num = 10
for i in range(0, 11):
    x = input("輸入四個顏色(以空白為間隔)")
    my = x.split()
    if len(my) == 4:
        OK = ""
        for u in range(0, 4):
            if my[u] == ans[u]:
                OK = OK + '1'
            elif my[u] in ans:
                OK = OK + '2'
            else:
                OK = OK + '3'
        num = num - 1
        if OK == '1111':
            print("答對了!")
            break
        elif num > 0:
            print(f"答錯了!，提示 : {OK}")
            print(f"你還有{num}次機會!")
        else:
            print("挑戰失敗!")
            break
    else:
        print("共4個顏色，請重新輸入!")