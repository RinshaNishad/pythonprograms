# qn1

# class Student:
#     name:str
#     age:int
#     grade:int

#     def __init__(self,name,age,grade):
#         self.name=name
#         self.age=age
#         self.grade=grade

#     def get_stud(self):
#         print(self.name,self.age,self.grade)


# std1=Student("Nyha",20,90)
# std1.get_stud()

# ================================================================================================================================

# qn2:


# class Staff:
#     name:str
#     salary:int
#     dept:str
#     desig:str

#     def __init__(self,name,salary,dept,desig):
#         self.name=name
#         self.salary=salary
#         self.dept=dept
#         self.desig=desig

#     def desg(self):
#         print(f"{self.name} is in {self.dept} dept")

        
# class Teacher(Staff):
#     def __init__(self,name,salary,dept,desig):
#         super().__init__(name,salary,dept,desig)
#     def desg(self):
#         print(f"{self.name} is in {self.dept} dept")

# obj1=Teacher("anu",25000,"cs","hod")
# obj2=Staff("manu",20000,"Office","hr")
# obj1.desg()
# obj2.desg()

# ================================================================================================================================

# qn3

# class Square:
#     num1:int
#     def __init__(self,n1):
#         self.num1=n1
#     def area(self):
#         return self.num1**2
#     def perimeter(self):
#         return self.num1*4
# ob1=Square(3)
# print(ob1.area()) 
# print(ob1.perimeter())

# ===================================================================================================================================

# qn4

# class Account:
#     def __init__(self,ac_name,ac_no, balance):
#         self.ac_name=ac_name
#         self.ac_no= ac_no
#         self.balance = balance




# ==============================================================================================================================

# qn5

# class Student:
#     rollno:int
#     name:str
#     course:str
#     year:int

#     def __init__(self,roll,name,course,year):
#         self.rollno=roll
#         self.name=name
#         self.course=course
#         self.year=year

#     def get_student(self):
#         print(self.rollno,self.name,self.course,self.year)

    

#     def display(self):
#         print("RollNo : ", self.rollno)
#         print("Name : ", self.name)
#         print("Course: ", self.course)
#         print("year: ", self.year)
        
     
# class Teacher:
#     id:int
#     name:str
#     dept:str

#     def __init__(self,id,name,dept):
#         self.id=id
#         self.name=name
#         self.dept=dept

#     def display(self):
#         print("id : ", self.id)
#         print("Name : ", self.name)
#         print("department: ", self.dept)
        
# class Course:
#     cname:str
#     duration:int

#     def __init__(self,cname,duration):
#         self.cname=cname
#         self.duration=duration

#     def display(self):
#         print("Course name : ", self.cname)
#         print("Duration: ", self.duration)
        
        

# ob=Student(1,"nunu","mca",3)
# ob.display()
# ob1=Student(2,"anu","bca",2)
# tr=Teacher(1,"AAdhi","CS")
# tr.display()
# ob.get_student()




    





