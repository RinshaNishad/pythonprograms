# num=30


# if(num % 15==0):
#     print("fizzbuzz")
# elif(num %5 == 0):
#     print("buzz")
# elif(num %3== 0):
#     print("fizz")        
#largest and second largest among three numbers
num1=10
num2=2
num3=30
if((num1>num2) and (num1>num3)):
    print(num1,"is largest")
    if(num2>num3):
        print(num2,"is second largest")
    else:
        print(num3,"is second largest")   

elif((num2>num1) and (num2>num3)):
    print(num2,"is largest")
    if(num1>num3):
        print(num1,"is second largest")
    else:
        print(num3,"is second largest")    
elif((num3>num1) and (num3>num2)):
    print(num3,"is largest") 
    if(num1>num2):
        print(num1,"is second largest")
    else:
        print(num2,"is second largest")


#sort these numbers(ascending or descending order)
if (num1>num2) and (num1 > num3):
    print((num3,num2,num1) if(num3<num2) else (num2,num3,num1))
elif (num2>num1) and (num2>num3):
    print((num1,num3,num2) if(num1<num3) else (num3,num1,num2))
elif(num3>num1) and (num3>num2):
    print((num1,num2,num3) if(num1<num2) else (num2,num1,num3))
else:
    print("wrong list")            
