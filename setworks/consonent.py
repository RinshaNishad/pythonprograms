word="Pneumonoultramicroscopicsilicovolcanoconios"
# print no. of vowels
vowels={"a","e","i","o","u"}
v_count=0
c_count=0
for ch in word:
    if ch in vowels:
        v_count+=1
    else:
        c_count+=1
print(v_count,": number of vowels")
print(c_count,": number of consonents")
            