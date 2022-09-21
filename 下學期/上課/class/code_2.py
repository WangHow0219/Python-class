class Person:
    def __init__(self):
        self.head=None
        self.body=None
        self.rhand=None
        self.lhand=None
        self.rleg=None
        self.lleg=None

class Head:
    def __init__(self,size):
        self.size=size
class Body:
    def __init__(self,capasity):
        self.capasity=capasity
class Hand:
    def __init__(self,length):
        self.length=length
class Leg:
    def __init__(self,length):
        self.length=length

Me=Person()
Me.head=Head(15)
Me.body=Body(65)
Me.rhand=Hand(80)
Me.lhand=Hand(80)
Me.rleg=Leg(90)
Me.lleg=Leg(90)

print(Me.head.size,"cm")
print(Me.body.capasity,"cm")

#----------------------------------------------

class Car:
    def __init__(self):
        self.engine=None
        self.tire=[]

class Engine:
    def __init__(self,cc):
        self.cc=cc
class Tire:#預設值
    def __init__(self,size=80):
        self.size=size

mazda=Car()
mazda.engine=Engine(4000)
for i in range(4):
    mazda.tire.append(Tire())

print(mazda.tire[0].size,"cm")