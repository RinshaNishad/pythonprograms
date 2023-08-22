# text="England promised to continue its aggressive approach to tst cricket"
#print the words starting with vowel

# txt=text.casefold()
# txt1=txt.split(" ")
# vowels=["a","e","i","o","u"]
# for t in txt1:
#     for v in vowels:
#         if t.startswith(v):
#             print(t)

#============================or===========================
txt="Elephants are big"
vowels=["a","e","i","o","u"]
words=txt.split()
for w in words:
    if w[0].casefold() in vowels:
        print(w)

ws=[w for w in txt.split(" ") if w[0].casefold() in vowels]
print(ws)