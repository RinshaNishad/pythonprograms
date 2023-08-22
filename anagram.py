word=input("enter a string :")
inpt=input("enter another word :")



srt_word=sorted(word)
srt_inpt=sorted(inpt)
# if srt_word==srt_inpt:
#     print("anagram")
# else:
#     print("non anagram")

print("anagram" if srt_word==srt_inpt else "not anagram")

#eg:fast,fats...ands,sand