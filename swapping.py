num1=10
num2=20
print(f"values b4 swapping num1={num1} num2={num2}")
#logic 1
# num1,num2=num2,num1 (only support on python) or


#logic 2
# temp=num1
# num1=num2
# num2=temp or


#logic 3
num1=num1+num2 #num1=10+20=30
num2=num1-num2 #num2=30-20=10
num1=num1-num2 #num1=30-10=20
print(f"values aftr swapping num1={num1} num2={num2}")