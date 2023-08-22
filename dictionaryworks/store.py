items = [
    {"sugar": 45},
    {"tea_powder": 28},
    {"coffee": 67},
    {"dairymilk": 170},
    {"kitkat": 70},
    {"bourborn": 50},
    {"munch": 30},
    {"milk": 80},
    {"pepsi": 99},

]

offers=[
    {"sugar":10},
    {"cofee":20},
    {"milk":5},
    {"pepsi":10}
]

#print todays selling price of all items
new={}
for item in items:
    for offer in offers:
        for k,v in item.items():
            for k1,v1 in offer.items():
                old_value=v
                offer_value=v1
                # if (k,k1) in new:
                #     old_value=new[k]
                if (k==k1) and (old_value>offer_value):
                    new[k1]=(old_value-offer_value)
                elif (k!=k1):
                    new[k]=old_value
print(new)












