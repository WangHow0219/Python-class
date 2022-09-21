class Person:
    def __init__(self,name,age,cm,kg):
        self.name = name
        self.age = age
        self.cm = cm
        self.kg = kg

group = []

f = open('C:/ALL/NKUST/VS_Code/程式設計/下學期/上課/CSV/data_個資.csv','r',encoding='utf-8')
Data = f.readlines()
for i in Data:
    tmp = i.split(',')
    name = tmp[0]
    age = int(tmp[1])
    cm = int(tmp[2])
    kg = int(tmp[3].split('\n')[0])
    tmp2 = Person(name,age,cm,kg)
    group.append(tmp2)
f.close
