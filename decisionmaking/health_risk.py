tummy_size=36
buttock_size=45
gender=0 or 1
value=tummy_size/buttock_size
print(value)
if gender==1: #and value<=0.80) or (gender==0 and value<=0.95)):
    if(value<=0.80):
        print("low risk")
    elif value<0.85:# or (gender==0 and value<1)):
        print("moderate risk")
    elif value>=0.85: #or (gender==0 and value>1)):
        print("high risk") 
else: 
    if gender == 0:
        if value<=0.95:
            print("low risk")
        elif value<1:
            print("moderate risk")
        elif value>1:
            print("high risk")
if(gender==0):
    print("male")
else:
    print("female") 