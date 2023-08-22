# print sum of digit in a given number


num=int(input("enter a number :"))
sum=0
while(num!=0):
    digit=num%10
    sum+=digit
    num=num//10
print(sum,"is the sum of digits")

