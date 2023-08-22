def smart_sub(n1,n2):
    return n1-n2 if n1>n2 else n2-n1
n1=int(input("enter num1 :"))
n2=int(input("enter num2 :"))
print(smart_sub(n1,n2))