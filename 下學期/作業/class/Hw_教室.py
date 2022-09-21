class ClassRoom:
    def __init__(self):
        self.tables=[]
        self.chairs=[]
        self.pcs=[]
        self.lights=[]

class Table:
    def __init__(self,length=240,width=80):
        self.length=length
        self.width=width
class Chair:
    def __init__(self,size=50,color="black"):
        self.size=size
        self.color=color
class PC:
    def __init__(self,cpu="Intel® Core™ i9-12900K",gpu="GeForce RTX 3090"):
        self.cpu=cpu
        self.gpu=gpu
class Light:
    def __init__(self,brightness=40):
        self.brightness=brightness

PC_ClassRoom=ClassRoom()
for i in range(3):
    PC_ClassRoom.tables.append(Table())
for i in range(3):
    PC_ClassRoom.chairs.append(Chair())
for i in range(3):
    PC_ClassRoom.pcs.append(PC())
for i in range(3):
    PC_ClassRoom.lights.append(Light())
    