def max_three(n1,n2,n3):
    return n1 if n1>n2 and n1>n3 else n2 if n2>n3 else n3
    # if (n1>n2) and (n1>n3):
    #     return n1
    # elif n2>n3:
    #     return n2
    # else:
    #     return n3
print(max_three(20,30,10))