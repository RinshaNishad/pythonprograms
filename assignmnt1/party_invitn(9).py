num=int(input("enter number of people:"))
if num<10:
    for i in range(1,num+1):
        name=input("enter name of person:")
        print(f"[{name}] has been invited..")
else:
    print("Too many people")