import re
sent="hi hello hi hi hello good 13, afternoon hi hello hide inhile 11:38,78"
ct=sent.count("hi")
print(ct)

#===============================or======================================

ct1=re.findall("hi",sent)
print(len(ct1))
#======================================================================
#==> check number below 60 in above sentence

nums=re.findall("[0-5][0-9]",sent)
print(nums)