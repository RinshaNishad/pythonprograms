class Books:
    name:str
    author:str
    price:int
    pages:int

    def __init__(self,**kwargs):
        self.name=kwargs.get("name")
        self.author=kwargs.get("author")
        self.price=kwargs.get("price")
        self.pages=kwargs.get("pages")

    def __str__(self):
        return self.name
    
obj=Books(name="Randamoozham",author="MT",price=600,pages=350)
print(obj)


#  __init__()==>constructor
#  __str__()==>strng representation
#  **kwargs==>dictionary format