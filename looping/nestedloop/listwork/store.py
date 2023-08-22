items=[
    [1,"potato",45,"veg",10],
    [2,"tomato",40,"veg",20],
    [3,"onion",35,"veg",0],
    [4,"brinjal",50,"veg",0],
    [5,"fish",145,"nonveg",10],
    [6,"chicken",145,"nonveg",10],
    [7,"egg",6,"nonveg",100]
]

#==> total number products
print(len(items),": total products")

#==> print in-stock prdct names
in_stock=[item[1] for item in items if item[4]>0 ]  #item[4]==item[-1]
print(in_stock,": products in stock")

#==> print out-of-stock prdct names
out_stock=[item[1] for item in items if item[4]==0]
print(out_stock,": products out of stock")

#==> print veg category prdct names
veg_categry=[item[1] for item in items if item[3]=="veg"] #item[3]==item[-2]
print(veg_categry,": products in veg category")

#==> prdct available in range of50-100
prdct_range=[item[1] for item in items if item[2] in range(50,101)]
print(prdct_range,": products in range 50-100")

#==> veg prdcts available in range of 40-80
veg_pdct=[item[1] for item in items if item[2] in range(40,81) and item[3]=="veg"]
print(veg_pdct,": veg pdct in range of 40 to 80")