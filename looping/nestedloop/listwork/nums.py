numbers=[2,7,8,9,12,13]
odds=[]
evens=[]
for num in numbers:
    evens.append(num) if num%2==0 else odds.append(num)
    # if num%2==0:
    #     even=num
    #     evens.append(num)
    # else:
        
    #     odds.append(num)
print("list of odd numbers :",odds)
print("list of even numbers",evens)
