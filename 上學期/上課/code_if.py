"""
多向式
if 條件1:
    程式區塊A
elif 條件2:
    程式區塊B
else 條件3:
    程式區塊C
"""
#note1_成績等第
score = int(input("輸入成績"))
if score >= 90:
    print("Tier A")
elif score >= 80:
    print("Tier B")
elif score >= 70:
    print("Tier C")
elif score >= 60:
    print("Tier D")
else:
    print("You are suck!")
