#Hw_if_郵資計算
kg = int(input("輸入重量 : "))
print("輸入重量 : " + str(kg) + "KG")
if kg <= 5:
    print("所需郵資為 50 元")
elif kg <= 10:
    print("所需郵資為 70 元")
elif kg <= 15:
    print("所需郵資為 90 元")
elif kg <= 20:
    print("所需郵資為 110 元")
else:
    print("超過 20 KG，無法寄送")

#Hw_if_BMI判斷
kg = int(input("輸入體重(KG) : "))
cm = int(input("輸入身高(cm) : "))
print("你的體重是 " + str(kg) + "KG")
print("你的身高是 " + str(cm) + "cm")
M = cm / 100
BMI = kg / M**2
print("BMI 為 : " + str(BMI))
if BMI < 18:
    print("體重過輕")
elif BMI <= 24:
    print("體重正常")
elif BMI <= 27:
    print("體重過重")
elif BMI >= 27:
    print("體重肥胖")

#Hw_if_打折條件
money = int(input("輸入購物金額 : "))
print("購物金額為 : " + str(money))
if money >= 100000:
    money = money * 0.8
    print("打折後是 : " + str(money))
elif money >= 50000:
    money = money * 0.85
    print("打折後是 : " + str(money))
elif money >= 30000:
    money = money * 0.9
    print("打折後是 : " + str(money))
elif money >= 10000:
    money = money * 0.95
    print("打折後是 : " + str(money))
else:
    print("金額不足打折門檻")

#Hw_if_數值判斷
A = int(input("輸入A值"))
B = int(input("輸入B值"))
C = int(input("輸入C值"))
print("A=" + str(A) + 
"  B=" + str(B) + "  C=" + str(C))
if A > B:
    if A > C:
        print("最大值為A")
    else:
        print("最大值為C")
elif B > C:
    print("最大值為B")
else:
    print("最大值為C")

#Hw_if_月份判斷
month = int(input("輸入月份"))
if 1 <= month <= 3:
    print(str(month) + "月是春天")
elif 4 <= month <= 6:
    print(str(month) + "月是夏天")
elif 7 <= month <= 9:
    print(str(month) + "月是秋天")
elif 10 <= month <= 12:
    print(str(month) + "月是冬天")
else:
    print(str(month) + "月不再範圍內")

#Hw_if_計算所得稅
Income = int(input("輸入今年收入 :"))
print("您今年收入為 : " + str(Income))
if Income >= 2000000:
    Income = Income * 0.3
    print("賦稅金額 : " + str(Income) + " 元")
elif Income >= 1000000:
    Income = Income * 0.21
    print("賦稅金額 : " + str(Income) + " 元")
elif Income >= 600000:
    Income = Income * 0.13
    print("賦稅金額 : " + str(Income) + " 元")
elif Income >= 300000:
    Income = Income * 0.06
    print("賦稅金額 : " + str(Income) + " 元")
else:
    print("免稅")

#Hw_if_象限判斷
X = int(input("輸入X座標 :"))
Y = int(input("輸入Y座標 :"))
print("輸入座標為 ("+str(X)+","+str(Y)+")")
if X == 0 and Y != 0:
    print("點在Y軸上")
elif Y == 0 and X != 0:
    print("點在X軸上")
elif Y == 0 and X == 0:
    print("此點是原點")
elif X > 0:
    if Y > 0:
        print("點在第一象限")
    else:
        print("點在第四象限")
else:
    if Y > 0:
        print("點在第二象限")
    else:
        print("點在第三象限")

#Hw_if_判斷發燒
c = float(input("輸入體溫 :"))
print("體溫為 : " + str(c))
if c < 36:
    print("體溫過低")
elif c < 38:
    print("體溫正常")
elif c < 39:
    print("體重微燒")
elif c >= 39:
    print("體重很燒")
