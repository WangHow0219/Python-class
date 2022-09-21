#ord
tmp='國立高雄科技大學鄭俊永王皓'
for i in tmp:
    print(hex(ord(i)))

num=65
x=list(range(6))
y=list(range(3))

for i in x:
    num = num+i
    print(num,end=" ")
    print()

A=65
for i in range(5):
    for j in range(i+1):
        print(65+i,end='')
    print()

#畫星星
#左
for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print()
#右
for i in range(5):
    for a in range(4-i):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()
#金字塔
for i in range(1,6):
    for a in range(5-i):
        print(" ",end="")
    for u in range(i+(i-1)):
        print("*",end="")
    print()
#金字塔_2
for i in range(1,6):
    for a in range(5-i):
        print(" ",end="")
    for u in range(i+(i-1)):
        if u%2==0:
            print(" ",end="")
        else:
            print("*",end="")
    print()
#菱形
for i in range(1,6):
    for a in range(6-i):
        print(" ",end="")
    for u in range(i+(i-1)):
        if u%2==0:
            print(" ",end="")
        else:
            print("*",end="")
    print()
for i in range(6,1,-1):
    for a in range(6-i):
        print(" ",end="")
    for u in range(i+(i-1)):
        if u%2==0:
            print(" ",end="")
        else:
            print("*",end="")
    print()

#蝴蝶
for i in range(1,6):
    for j in range(i):
        print("*",end="")
    for k in range(5-i):
        print("  ",end="")
    for l in range(i):
        print("*",end="")
    print()
for i in range(4,0,-1):
    for j in range(i):
        print("*",end="")
    for k in range(5-i):
        print("  ",end="")
    for l in range(i):
        print("*",end="")
    print()

#幾A幾B
hcy="0927"
abc=input("輸入4位數字")
a=0
b=0
if hcy==abc:
    print("true")
for i in range(4):
    if abc[i] == hcy[i]:
        a=a+1
    elif abc[i] in hcy:
        b=b+1
print(a,"A",b,"B")
