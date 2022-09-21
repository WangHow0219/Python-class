#tuple
list_1=[1,2,3,4]
tuple_1=(1,3,5)
print(tuple_1[1])
tuple_2 = tuple(list_1)

print("-------------------")

#random.randint
#隨機分數
import random
grade=[]
for i in range(1,11):
    grade.append(random.randint(60,100))
print(grade)

print("-------------------")

#format
#製作學號
num="C2"
ID=[]
for i in range(1,11):
    ID.append(num + "{0:02d}".format(i))
print(ID)

print("-------------------")

#dictionary
IdGrade={"C201":{"國文":60,"英文":65},"C202":90,"C203":{}}

IdGrade["C202"]=50
IdGrade["C203"]["英文"]=99

print(IdGrade["C202"])
print(IdGrade["C201"]["英文"])

print("-------------------")

#把 2個 list合併成一個 dict
IdGrade_OK={}
for u in range(0,10):
    IdGrade_OK[ID[u]]=grade[u]
