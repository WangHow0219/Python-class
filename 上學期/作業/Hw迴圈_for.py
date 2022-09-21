#Hw_1
a = int(input("輸入一整數"))
list1 = range(1, a+1)
print(list(list1))

print("------------------------------------------")

#Hw_2
b = int(input("輸入一整數"))
all1 = 0
for B in range(1, b+1):
    all1 = all1 + B
print(f"1 到 {b}的整數和為 {all1}")

print("------------------------------------------")

#Hw_3
start = int(input("輸入開始值"))
end = int(input("輸入終止值"))
add = int(input("輸入增減值"))
all2 = 0
for R in range(start, end+1, add):
    all2 = all2 + R
print(f"從{start}到{end}")
print(f"間隔為{add}的加總值為:{all2}")

#Hw_4 排除 5 的倍數
d = int(input("輸入一整數"))
e = (5,10,15,20,25,30,35,40,45,50,55,60,65,70)
for T in range(1, d+1):
    if T not in e:
        print(f"{T} ",end="")


