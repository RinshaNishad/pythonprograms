class Bank:
    acno:int
    balance:int
    ac_type:str
    p_name:str

    def create_acnt(self,acno,blnc,ac_type,name):
        self.acno=acno
        self.balance=blnc
        self.ac_type=ac_type
        self.p_name=name

    def deposit(self,amount):
        self.balance+=amount
        print(f"your sbk acnt {self.acno} has been credited with {amount} avail blnc is {self.balance}")

    def withdraw(self,amount):
        if self.balance >=amount:
            self.balance-=amount
            print(f"your sbk acnt {self.acno} has been debited with {amount} avail blnc is {self.balance}")
        else:
            print("transaction failed insufficient bal")

    # def display_acnt(self):
    #     print(self.acno,self.balance,self.ac_type,self.p_name,self.amount,self.amount)

cust1=Bank()
cust1.create_acnt(1234,5000,"savings","ammu")
# cust1.deposit(50000)
cust1.withdraw(3000)






