#迴圈
    #range : 
    #range(終止值)
    #range(起始值,終止值)
    #range(起始值,終止值,間格值)
list1 = range(5)
print(list(list1))

list2 = range(3,8)
print(list(list2))

list3 = range(3, 8, 2)
print(list(list3))

list4 = range(8, 3, -1)
print(list(list4))

list5 = range(-2, 4)
print(list(list5))

list6 = range(5, 1, 1)
print(list(list6))

"""
for迴圈
用於執行固定次數
語法 : 
for 變數 in 串列
    程式區塊
"""

#note_1
list7 = ["A", "B", "C"]
for a in list7:
    print(a)

#note_2
sum1 = 0
for i in range(1, 11):
    sum = sum + i
print(sum)

#note_ n! (for)
toatl1 = i = 1
n = int(input("輸入整數"))
for i in range(1, n+1):
    toatl1 = toatl1 * i    
print(f"{n}! = {toatl1}")
