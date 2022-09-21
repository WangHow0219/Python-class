# Hw_class-高科大
class NKUST:
    def __init__(self):
        self.campus=[]
class Campus:
    def __init__(self,campus):
        self.campus=campus
        self.department=[]
class Department:
    def __init__(self,department):
        self.department=department
        self.grade=[]
class Grade:
    def __init__(self,grade):
        self.grade=grade
        self.student=[]
class Student:
    def __init__(self,student):
        self.student=student

Man=NKUST()
Man.campus=Campus("燕巢")
Man.campus.department=Department("智商")
Man.campus.department.grade=Grade("一年級")
Man.campus.department.grade.student=Student("王皓")
