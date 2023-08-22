items=[
    {"name":"biriyani","price":130,"category":"nonveg"},
    {"name":"dosa","price":70,"category":"veg"},
    {"name":"vegfriedrice","price":130,"category":"veg"},
    {"name":"noodles","price":130,"category":"nonveg"},
    {"name":"burger","price":130,"category":"nonveg"},
    
]

#==> print all item names

item_names=list(map(lambda it:it.get("name"),items))
print(item_names)
    #==============using lst comprehension=====================
lst_itemnames=[it.get("name") for it in items]
print(lst_itemnames)
#=================================================================
#==>print price of all items

price=list(map(lambda it:it.get("price"),items))
print(price)
                #using lst cmprhnsn
lst_price=[it.get("price") for it in items]
print(lst_price)
#===================================================================
filter_veg=list(filter(lambda it:it.get("category")=="veg",items))
print(filter_veg)

list_veg=[it.get("name") for it in items if it.get("category")=="veg"]
print(list_veg)
#======================================================================
