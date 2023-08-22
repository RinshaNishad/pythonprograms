class P1:
    def m1(self):
        print("class p1 m1 method")

class P2:
    # def m2(self):
    def m1(self):
        print("class p2 m1 method")
        # print("class p2 m2 method")

# class C1(P1,P2):
class C1(P2,P1):
    pass

c=C1()
c.m1()
# c.m2()