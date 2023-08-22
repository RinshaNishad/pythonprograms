num=1634
org=num
cnt=len(str(num))
sum=0
while num!=0:
    digit=num%10
    sum+=digit**cnt
    num=num//10

if (sum==org):
    print(org,"is an amstrong number")
else:
    print(org,"is not an amstrong number")