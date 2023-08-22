wgt=54
hgt_cm=160
hgt_m=hgt_cm/100
bmi=(wgt/ (hgt_m )** 2)
print(bmi)
if((bmi< 18.5)):
    print("underweight")
elif bmi <= 24.9 :       #elif((bmi>=18.5) & (bmi<=24.9)): 
    print("normalweight")
elif bmi <= 29.9:         #elif((bmi>=25.0) & (bmi<=29.9)):  
    print("overweight")
elif bmi <= 34.9:         #elif((bmi>=30.0) & (bmi<=34.9)):
    print("obesity class 1")        
elif bmi <= 39.9:         #elif((bmi>=35.0) & (bmi>=39.9)):
    print("obesity class 2")
else:                      #elif((bmi>=40)):                 
    print("obesity class 3") 
         


