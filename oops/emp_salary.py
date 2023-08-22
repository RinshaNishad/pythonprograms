from abc import ABC,abstractmethod
class Employee(ABC):
    name:str
    salary:int

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    @abstractmethod
    def calculate_salary(self):
        pass

class Manager(Employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)
    def calculate_salary(self):
        return self.salary+25000
       
class Developer(Employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)
    def calculate_salary(self):
        return self.salary+20000

obj=Developer("anu",25000)
print(obj.calculate_salary())

    

