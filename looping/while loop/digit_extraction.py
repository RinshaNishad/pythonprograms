#prgm to prnt digits in a number


num=123

while(num!=0):   #123!=0  12!=2       1!=0      0!=0
    digit=num%10 #123%10=3  12%10=2   1%10=1   
    print(digit) #3          2         1
    num=num//10  #123//10=12 12//10=1  1//10=0
    