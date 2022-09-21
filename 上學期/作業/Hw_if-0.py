#作業_迴文判斷
print("-------------------------")
word1 = input("輸入一個字串 : ")
N1 = (word1[::-1])
print("迴文判斷結果為 :", word1==N1)
print("-------------------------")
    
#作業_if_打折判斷
money = int(input("請輸入購買金額 : "))
print("你買了" + str(money) + "元的商品")
if money >= 2000:
    money = money * 0.9
    print("打9折後是 :" + str(money))
else:
    print("這樣總共是 : " + str(money))
print("-------------------------")

#作業_if_奇偶數判斷
number = int(input("請輸入一整數 : "))
print("你的數字是:" + str(number))
if number % 2 == 1:
    print(str(number) + "為奇數")
else:
    print(str(number) + "為偶數")
print("-------------------------")

#作業_if_三角形判斷
A = int(input("輸入三邊長A"))
B = int(input("輸入三邊長B"))
C = int(input("輸入三邊長C"))
print("你輸入的三邊長為" + 
" A:" + str(A) + " B:" + str(B) + " C:" + str(C))
if A + B > C and B + C > A and C + A > B:
    print("可構成三角形")
else:
    print("無法構成三角形")
print("-------------------------")