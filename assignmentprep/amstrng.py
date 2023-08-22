num=int(input("Enter a number:"))
org=num

int=len(str(num))
sum=0
while num!=0:
    digit=num%10
    sum+=digit**int
    num=num//10
if org==num:
    print(org,"is an amstrng no")
else:
    print(org,"is not an armstrong no")