# class Student:
#     rollno:int
#     name:str
#     course:str
#     year:int

#     def add_student(self,roll,name,course,year):
#         self.rollno=roll
#         self.name=name
#         self.course=course
#         self.year=year

#     def get_student(self):
#         print(self.rollno,self.name,self.course,self.year)

# std1=Student()

# std1.add_student(11,"Ammu","MCA",2)
# std1.get_student()

# std2=Student()

# std2.add_student(13,"Manu","BCA",1)
# std2.get_student()

#=====================================================================
#constructor method
#duty==> initializing instance variable self.roll,silf.name....
#constructor name is always..__init__



class Student:
    rollno:int
    name:str
    course:str
    year:int

    def __init__(self,roll,name,course,year):
        #initializing instance variable==>constructor
        self.rollno=roll
        self.name=name
        self.course=course
        self.year=year

    def get_student(self):
        print(self.rollno,self.name,self.course,self.year)

std1=Student(11,"Ammu","MCA",2)
std1.get_student()

std2=Student(13,"Manu","BCA",1)
std2.get_student()