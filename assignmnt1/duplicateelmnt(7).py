lst=[2,3,4,4,5,5,6,7,1,7,9]

x = []
y = []
for i in lst:
    if i not in x:
        x.append(i)
for i in x:
    if lst.count(i) > 1:
        y.append(i)
print("duplicate elements are :",y)
