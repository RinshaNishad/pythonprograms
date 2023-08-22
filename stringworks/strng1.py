text="one 100 and fifty 5"
#100,5
# words=text.split(" ")
# for w in words:
#     if w.isdigit():
#         print(w)

nums=[w for w in text.split(" ") if w.isdigit()]
print(nums)
