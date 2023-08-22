from re import *
tweets="What a game , hats off to both teams . Well done @benstokes38 @patcummins30 you have bought test cricket back to life. Love test cricket  @TheBarmyArmy @CricketAus @ECB_cricket"
# rule="[@]{1}[a-zA-Z0-9_]+"
# # rule="@\S+"
# matcher=findall(rule,tweets)
# print(matcher)

#===============================or===============================

rule="[@]{1}[a-zA-Z0-9_]+"
# rule="@\S+"
matcher=finditer(rule,tweets)
for m in matcher:
    print(m.group())


#  +----atleast one time
#  *----any no of time




    