#Hw_if_分數判斷pro
P1 = int(input("輸入期中考分數"))
P2 = int(input("輸入期末考分數"))
Pall = P1*0.4 + P2*0.6
if Pall <0 or Pall >100:
    print("輸入分數有誤")
else:
    if Pall >= 90:
        print("總分:"+str(Pall)+"  A")
    elif Pall >= 80:
        print("總分:"+str(Pall)+"  B")
    elif Pall >= 70:
        print("總分:"+str(Pall)+"  C")
    elif Pall >= 60:
        print("總分:"+str(Pall)+"  D")
    else:
        print("總分:"+str(Pall)+"  E")

#Hw_if_象限判斷
X = float(input("輸入X座標 :"))
Y = float(input("輸入Y座標 :"))
print(f"輸入座標為({X:5.1f},{Y:5.1f})")
if X == 0 and Y != 0:
    print("點在Y軸上")
elif Y == 0 and X != 0:
    print("點在X軸上")
elif Y == 0 and X == 0:
    print("此點是原點")
elif X > 0:
    if Y > 0:
        print("第I象限")
    else:
        print("第IV象限")
else:
    if Y > 0:
        print("第II象限")
    else:
        print("第III象限")

#Hw_if_車種罰金判斷
car = input("輸入車種(B or C)")
print("車輛種類 :" + str(car))
over = float(input("輸入超速公里數"))
print(f"超速公里數 : {over:.2f}")
if car == "B":
    if over <20:
        print("罰金1,200")
    elif over <40:
        print("罰金1,400")
    elif over <60:
        print("罰金1,600")
    elif over <80:
        print("罰金8,000")
    elif over <100:
        print("罰金12,000")
    else:
        print("罰金24,000")
elif car == "C":
    if over <20:
        print("罰金1,600")
    elif over <40:
        print("罰金1,800")
    elif over <60:
        print("罰金2,000")
    elif over <80:
        print("罰金8,000")
    elif over <100:
        print("罰金12,000")
    else:
        print("罰金24,000")
else:
    print("請輸入正確車種")