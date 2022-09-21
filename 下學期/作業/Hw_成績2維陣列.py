import random
#製作學號
ID=[]
for i in range(1,11): # 1到 10
    ID.append("C" + "{0:02d}".format(i))

#三科目list
suject=["國文","英文","數學"]

#宣告 分數變數
grade=0

#宣告 dict
IdGrade_Pro={}
for i in range(0,10):
    IdGrade_Pro[ID[i]] = {}
    for u in range(0,3):
        #每次輸入隨機分數
        grade = random.randint(60,100)
        IdGrade_Pro[ID[i]][suject[u]] = grade
