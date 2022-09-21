#Hw_1 N!超過 M 的最小 N 值為何？\
max = int(input("輸入最大值"))
toatl_1 = 1
n = 1
while (toatl_1 <= max):
    toatl_1 = toatl_1 * n
    n = n + 1
n = n - 1
print(f"{n}! = {toatl_1} , 大於 {max}")

#Hw_2 偶數總和,奇數總和,3及7的倍數的總和&比較上續大小
n = int(input("輸入一整數"))
print(f"你輸入的數為{n}")
toatl_A=toatl_B=toatl_C = 0
pa = 2
while (pa<=n):
    toatl_A = toatl_A + pa
    pa = pa + 2
print(f"偶數合為{toatl_A}")
pb = 1
while (pb<=n):
    toatl_B = toatl_B + pb
    pb = pb + 2
print(f"奇數合為{toatl_B}")
pc = 21
while (pc<=n):
    toatl_C = toatl_C + pc
    pc = pc + 21
print(f"3及7的公倍數合為{toatl_C}")
if  toatl_A > toatl_B > toatl_C:
    print("偶數合>奇數合>3及7的公倍數合")
elif toatl_A > toatl_C > toatl_B:
    print("偶數合>3及7的公倍數合>奇數合")
elif toatl_B > toatl_A > toatl_C:
    print("奇數合>偶數合>3及7的公倍數合")
elif toatl_B > toatl_C > toatl_A:
    print("奇數合>3及7的公倍數合>偶數合")
elif toatl_C > toatl_A > toatl_B:
    print("3及7的公倍數合>偶數合>奇數合")
elif toatl_C > toatl_B > toatl_A:
    print("3及7的公倍數合>奇數合>偶數合")

#Hw_3 模擬帳號與密碼登入
user = input("輸入帳號")
key = input("輸入密碼")
while (user != key):
    print("帳號與密碼不一致!請重新輸入")
    user = input("輸入帳號")
    key = input("輸入密碼")
print("帳號與密碼正確!登入成功")

#Hw_4 請輸入一正整數n，印出因數及判斷是否為質數
n = int(input("輸入一整數"))
i = 1
s = 0
print(f"{n}的因數有: ",end="")
while (n >= i):
    if n % i == 0:
        print(f"{i} ",end="")
        s = s + 1
    i = i + 1
print("")
if s == 2:
    print(f"{n} 是質數")
else:
    print(f"{n}不是質數")
