from abc import ABC,abstractmethod
class Bike:
    name:str
    model:str
    fuel_type:str
    def __init__(self,name,model,fuel_type):
        self.name=name
        self.model=model
        self.fuel_type=fuel_type

    @abstractmethod
    def start(self):
        pass

class Hunter(Bike):
    def __init__(self,name,model,fuel_type):
        super().__init__(name,model,fuel_type)
    def start(self):
        print(f"{self.name}starting model {self.model} fuel {self.fuel_type}")

# class Ather(Bike):
hun=Hunter("hunter dapper grey","2023","petrol")
hun.start()
