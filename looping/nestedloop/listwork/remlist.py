birds=["peacock","duck","hen","kiwi"]
ch_name=input("Enter a bird :")
for i in birds:
    if i==ch_name:
        birds.remove(i)
print(birds)