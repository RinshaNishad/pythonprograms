from json import load

with open("C:\\Users\\DELL\\Desktop\\pythonworks\\restCountries\\rest.json","r",encoding="UTF") as f:
    data=load(f) 

#==> total number of countries
# print(len(data))
#==============================================

#==>print all country names
# names=[c.get("name") for c in data]
# print(names)
#===============================================

#==>print all region names
# region_names={c.get("region") for c in data}
# print(region_names)
#=================================================

#==> print asian country names
# asian_country=[c.get("name") for c in data if c.get("region")=="Asia"]
# print(asian_country)
# print(len(asian_country))
#========================================================

#==> print population of afghanistan
# popltn_afgnstn=[c.get("population") for c in data if c.get("name")=="Afghanistan"]
# print(popltn_afgnstn)
#==========================================================

#==>print indian borders
# borders=[c.get("borders") for c in data if c.get("name")=="India"][0]
# print(borders)

# border_names=[c.get("name") for c in data if c.get("alpha3Code") in borders]
# print(border_names)
#===================================================================

#==>print currency code
# curr_code=[c.get("currencies") for c in data if c.get("name")=="India"][0]
# print(curr_code)

# multi_curr_country=[c.get("name")for c in data if len(c.get("currencies"))>1]
# print(multi_curr_country)
#=====================================================================


# cntry with highst popltn

high_popltn=max(data,key=lambda k:int(k.get("population")))
print(high_popltn)


