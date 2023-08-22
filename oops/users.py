class Users:
    data=[
        {"id":1,"username":"jhon","email":"jhon@gmail.com","password":"password@123"},
        {"id":2,"username":"hari","email":"hari@gmail.com","password":"password@123"},
        {"id":3,"username":"ravi","email":"ravi@gmail.com","password":"password@123"},
        {"id":4,"username":"vijay","email":"vijay@gmail.com","password":"password@123"},
        {"id":5,"username":"vinu","email":"vinu@gmail.com","password":"password@123"},
        {"id":6,"username":"tom","email":"tom@gmail.com","password":"password@123"},
    ]

    def get(self):
        return self.data
    
    def retrieve(self,id):
        return [u for u in self.data if u.get("id")==id]
    
    def post(self,obj):
        self.data.append(obj)

    def destroy(self,id):
        obj=[u for u in self.data if u.get("id")==id][0]
        self.data.remove(obj)

    def put(self,id,value):
        obj=[u for u in self.data if u.get("id")==id][0]
        print(value)
        pos=self.data.index(obj)
        self.data[pos]=value
        



obj=Users()
#==for get function(create)
print(obj.get())
#================================

#================================
#===for post function(insrt new id)===
stud_data={"id":7,"username":"anu","email":"anu@gmail.com","password":"ruhi@123"}
obj.post(stud_data)
# print(obj.get())
#====================================

#====for destroy function(remove/delete)
obj.destroy(5)
# print(obj.get())
#======================================

data={"id":7,"username":"anus","email":"anu@gmail.com","password":"ruhi@123"}
obj.put(7,data)
print(obj.retrieve(7))



# get()---list details
#retrieve(id)---return detail
# post()---create/insert detail
# put(id)----update detail
# destroy(id)---remove/delete