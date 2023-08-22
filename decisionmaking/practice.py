num1=100
num2=20
num3=30
if((num1>num2) and (num1>num3)):
    if(num2>=num3):
        print(num2,"is second largest")
    else:
        print(num3,"is second largest")
elif((num2>num1) and (num2>num3)):
    if(num1>=num3):
        print(num1,"is second largest")
    else:
        print(num3,"is second largest")
elif((num3>num1) and (num3>num2)):
    if(num1>=num2):
        print(num1,"is second largest")
    else:
        print(num2,"is second largest")

if(num1>num2) and (num1>num3):
    if(num3<num2):
        print(num3,num2,num1)
    else:
        print(num2,num3,num1)
elif(num2>num1) and (num2>num3):
    if(num1<num3):
        print(num1,num3,num2)
    else:
        print(num3,num1,num2)
elif(num3>num1) and (num3>num2):
    if(num1<num2):
        print(num1,num2,num3)
    else:
        print(num2,num1,num3)                            

