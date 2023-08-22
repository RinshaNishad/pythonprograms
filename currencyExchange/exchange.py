# rates={
#     "USD": 1,
#     "AED": 3.6725,
#     "AFN":86.0330,
#     "ALL":97.5499,
#     "AMD":386.9256,
#     "ANG":1.7900,
#     "AOA":824.0658,
#     "ARS":254.7465,
#     "AUD":1.5099,
#     "AWG":1.7900,
#     "AZN":1.6979,
#     "BAM":1.7974,
#     "INR":82.0914
# }

# # # currency exchange rate application

# amount=int(input("enter amount you want to exchange :"))
# fromCurrencyCode=input("enter source currency code :")
# toCurrencyCode=input("enter designation currency code:")
# #eqn=(amount/from_currency_code-rate)*to_currency_code_rate
# from_code_rate=rates.get(fromCurrencyCode)
# to_currency_code_rate=rates.get(toCurrencyCode)
# result=(amount/from_code_rate)*to_currency_code_rate
# print(result)
#===========================================================================

from json import load
with open("C:\\Users\\DELL\\Desktop\\pythonworks\\currencyExchange\\db.json","r",encoding="UTF") as f:
    data=load(f)

# print(data)

rates=data.get("conversion_rates")
# print(rates)

amount=int(input("enter amount you want to exchange :"))
from_cur_code=input("enter source currency code :")
to_cur_code=input("enter designation currency code:")

from_rate=rates.get(from_cur_code)
to_rate=rates.get(to_cur_code)
result=(amount/from_rate)*to_rate
print(result)


