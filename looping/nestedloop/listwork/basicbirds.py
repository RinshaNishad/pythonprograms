#create a list of 5 birds,print one by one,chage third bird to penguin

birds=["parrot","cuckoo","hen","ostrich","kiwi"]
print(birds)
birds[2]="penguin"
print(birds)
#check for third element,if it is penguin change it to "am penguin"
if(birds[2]=="penguin"):
    birds[2]="Am penguin"
else:
    birds[2]="Am not penguin"
print(birds)
