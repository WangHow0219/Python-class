# Person
class Person:
    def __init__(self,name,male,alter):
        self.__name=name
        self.__male=male
        self.__alter=alter
    
    def print_beschreibung(self):
        return(None)

    #setter & getter
    def set_alter(self,alter):
        self.__alter=alter
    
    def get_alter(self):
        return self.__alter

    def get_male(self):
        return self.__male
    
    def get_name(self):
        return self.__name

Me = Person("How",True,180)
print(Me.get_alter())
Me.set_alter("169")
print(Me.get_alter())
