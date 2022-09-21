class Car_Toyata:
    def __init__(self):
        self.engine=None
        self.fr_tire=None
        self.fl_tire=None
        self.br_tire=None
        self.bl_tire=None

class Engine:
    def __init__(self,cc):
        self.cc=cc
class Tire:
    def __init__(self,size):
        self.size=size

toyota=Car_Toyata()
toyota.engine=Engine(2000)
toyota.fr_tire=Tire(45)
toyota.fl_tire=Tire(45)
toyota.br_tire=Tire(45)
toyota.bl_tire=Tire(45)

#--------------------------------------

class Car_Posh:
    def __init__(self):
        self.engine=None
        self.tires=[]

class Tires:
    def __init__(self,size=50):
        self.size=size

Posh = Car_Posh()
Posh.engine = Engine(3000)
for i in range(4):
    Posh.tires.append(Tires())