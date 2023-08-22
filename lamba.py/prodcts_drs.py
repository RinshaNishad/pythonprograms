clothes=[
    {"material":"linen","name":"uspoloshirt","cost":3000,"sizes":["s","m","l"],"brand":"uspolo","colors":["white","black"]},
    {"material":"cotton","name":"lpshirt","cost":4000,"sizes":["s","m","l"],"brand":"louisphilip","colors":["blue","green","black"]},
    {"material":"linen","name":"arrow tshirts","cost":3500,"sizes":["s","l"],"brand":"arrow","colors":["green","yellow"]},
    {"material":"linen","name":"jeans","cost":2500,"sizes":["s","m","l"],"brand":"wrangler","colors":["black","grey"]},
    {"material":"linen","name":"tshirts","cost":1500,"sizes":["m","l"],"brand":"benetton","colors":["white","green"]},

]

#==> print all Name
for c in clothes:
    print(c.get("name"))

#==> print uspolo brand details
for c in clothes:
    if "uspolo" in c.get("brand"):
        print(c)
#==> print costly item
print(max(clothes,key=lambda c:c.get("cost")))