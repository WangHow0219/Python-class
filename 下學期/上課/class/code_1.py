#class is an user-defined data type, and compose of
#attributes(fidlds,data memeber)and fuction(methods)

class Teacher:
    # constructor
    def __init__(self,name,weight,height):
        self.name=name
        self.weight=weight
        self.height=height
    
    def eat(self):
        self.weight = self.weight + 1
    
    def run(self):
        self.weight = self.weight - 0.5

Man1 = Teacher("黃河全",70,170)
print(Man1.name)
print(Man1.weight)

Man1.eat()
print(Man1.weight)

Man2 = Teacher("黃天受",80,180)
Man2.run()

Man3 = Teacher("謝文川",70,169)

