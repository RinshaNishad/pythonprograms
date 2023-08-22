class Employee:

    id:int
    name:str
    desig:str
    salary:str

    def set_emp(self,id,name,desig,salary):
        self.id=id
        self.name=name
        self.desig=desig
        self.salary=salary

    def get_emp(self):
        print(self.id,self.name,self.desig,self.salary)


emp1=Employee()

emp1.set_emp(100,"Nyha","hr",45000)
emp1.get_emp()

emp2=Employee()
emp2.set_emp(101,"Nishad","developer",40000)
emp2.get_emp()