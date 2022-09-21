# Author
class Author:
    def __init__(self,name,email,gender):
        self.__name=name
        self.__email=email
        self.__gender=gender

    def getName(self):
        return self.__name
    
    def getEmail(self):
        return self.__email

    def setEmail(self,email):
        self.__email=email

    def getGender(self):
        return self.__gender

    def print(self):
        pass

Me=Author("How","how@gmail.com","男")
print(Me.getEmail())
Me.setEmail("wanghow@gmail.com")
print(Me.getEmail())
