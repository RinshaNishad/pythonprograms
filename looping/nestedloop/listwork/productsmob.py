mobiles=[
    [100,"redminote12",23000,"5g"],
    [101,"oneplusnord",32000,"5g"],
    [102,"iphone14",123000,"5g"],
    [103,"s23ultra",133000,"5g"],
    [104,"pixel12",43000,"5g"],
    [105,"nothing",13000,"4g"],
    [106,"galaxya52",23000,"5g"]
        
]

#==>total number of mobiles
print(len(mobiles),"mobiles available")

#==> print all mobile names

# for mob in mobiles:
#     print(mob[1])
#---------------------------------------
mobile_names=[mob[1] for mob in mobiles]
print(mobile_names)

#==> print 4g mobile names

mobile_range=[mob[1] for mob in mobiles if mob[3]=="4g"]
print(mobile_range)
#-------------------------------------------------------------

# for mob in mobiles:
#     if mob[3]=="4g":
#         print(mob[1])


#==> print mobile names price<3oooo


mobile_price=[mob[1] for mob in mobiles if mob[2]<30000]
print(mobile_price)


#==>  print mobile names available in range of 30000 to 50000

# mobile_avail=[mob[1]for mob in mobiles if mob[2]>30000 and mob[2]<50000]
# print(mobile_avail)

# mobile_avail=[mob[1]for mob in mobiles if 30000<mob[2]<50000]
# print(mobile_avail)

mobile_avail=[mob[1]for mob in mobiles if mob[2] in range(30000,50001)]
print(mobile_avail)

#==> print all 5g mobiles under  25000

price_ntwrk=[mob[1] for mob in mobiles if mob[2]<25000 and mob[3]=="5g"]
print(price_ntwrk)





