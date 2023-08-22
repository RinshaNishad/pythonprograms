class Student:
    rollno:int
    name:str
    course:str

    def __init__(self,**kwargs):
        self.rollno=kwargs.get("rollno")
        self.name=kwargs.get("name")
        self.course=kwargs.get("course")

    def get_student(self):
        print(self.rollno,self.name,self.course)

    def __str__(self):      #} code to print obj name(string rprsntstn)
        return self.name    #}


obj=Student(rollno=100,name="anu",course="django")

obj.get_student()
print(obj)
