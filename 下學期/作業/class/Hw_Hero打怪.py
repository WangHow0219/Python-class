import random

class Student:
    def __init__(self,name,hp,atk):
        self.name=name
        self.hp=hp
        self.atk=atk

    def attack(self,unatker):
        unatker.hp = unatker.hp-self.atk
    def unattack(self,atker):
        self.hp = self.hp - atker.atk

wanghow = Student("醜王皓",500,30)
junyong = Student("俊永",900,10)

wanghow.attack(junyong)
print(junyong.hp)

wanghow.unattack(junyong)
print(wanghow.hp)

print("---------------------------------------------")

class Game:
    def __init__(self,name,hp,atk):
        self.name=name
        self.hp=hp
        self.atk=atk
    def attack(self,unatker):
        unatker.hp -= self.atk
    def unattack(self,atker):
        self.hp = self.hp - atker.atk

Hero = Game("Hero",1000,100)
MstGroup=[]
for i in range(5):
    MstGroup.append(Game('m'+str(i+1),random.randint(100,150),random.randint(20,40)))

Hero.attack(MstGroup[random.randint(0,4)])
Hero.attack(MstGroup[random.randint(0,4)])
Hero.attack(MstGroup[random.randint(0,4)])

for i in range(5):
    MstGroup[random.randint(0,4)].attack(Hero)
    print('m'+str(i+1)+' Hp:',end="")
    print(MstGroup[i].hp)
print(Hero.hp)