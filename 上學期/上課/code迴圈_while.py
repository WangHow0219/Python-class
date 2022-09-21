"""
while loop
用於執行次數不固定的迴圈
語法 : 
while 條件式:
        程式區塊
"""
#note_累加器1
toatl1 = n = 0
while (n<10):
    n = n + 1
    toatl = toatl + n
print(toatl)

#note_ n! (while)
toatl2 = i = 1
n = int(input("輸入整數"))
while (i<=n):
    toatl2 = toatl2 * i
    i = i + 1
print(f"{n}! = {toatl2}")