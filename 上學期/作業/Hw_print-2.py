#作業 - 基本 input & print
f1 = int(input("輸入薪資:"))
f2 = int(input("輸入獎金:"))
f3 = int(input("輸入加班費:"))
T = f1 + f2 + f3
print("輸入薪資:" + str(f1))
print("輸入獎金:" + str(f2))
print("輸入加班費:" + str(f3))
print("本月時領金額:" + str(T))

print("------------------------------------------")

#作業 - 用 input & print 列印整齊表格_1
NA = input("輸入姓名1:")  #林大名
nA = input("輸入座號1:")
PA1 = input("輸入國文成績:")
PA2 = input("輸入數學成績:")
PA3 = input("輸入英文成績:")
#--------------------------------------------
NB = input("輸入姓名2:")  #陳阿忠
nB = input("輸入座號2:")
PB1 = input("輸入國文成績:")
PB2 = input("輸入數學成績:")
PB3 = input("輸入英文成績:")
#--------------------------------------------
NC = input("輸入姓名3:")  #張小英
nC = input("輸入座號3:")
PC1 = input("輸入國文成績:")
PC2 = input("輸入數學成績:")
PC3 = input("輸入英文成績:")
#--------------------------------------------
print("姓名   座號   國文  數學  英文")
print("%s %4s %5s %5s %5s" % (NA, nA, PA1, PA2, PA3))
print("%s %4s %5s %5s %5s" % (NB, nB, PB1, PB2, PB3))
print("%s %4s %5s %5s %5s" % (NC, nC, PC1, PC2, PC3))

print("------------------------------------------")

#作業 - 用 input & print 列印整齊表格_2
YA = input("輸入年度:")
MA1 = float(input("所的稅:"))
MA2 = float(input("營業稅:"))
MA3 = float(input("證交稅:"))
#-------------------------------------
YB = input("輸入年度:")
MB1 = float(input("所的稅:"))
MB2 = float(input("營業稅:"))
MB3 = float(input("證交稅:"))
#-------------------------------------
YC = input("輸入年度:")
MC1 = float(input("所的稅:"))
MC2 = float(input("營業稅:"))
MC3 = float(input("證交稅:"))
#------------------------------------- 
print("年度   所得稅   營業稅   證交稅")
print("%s% 8.2f% 9.2f% 9.2f" % (YA, MA1, MA2, MA3))
print("%s% 8.2f% 9.2f% 9.2f" % (YB, MB1, MB2, MB3))
print("%s% 8.2f% 9.2f% 9.2f" % (YC, MC1, MC2, MC3))

print("------------------------------------------")
