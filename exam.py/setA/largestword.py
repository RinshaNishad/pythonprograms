txt="pycharm is       an ide"

word=txt.split(" ")

print(max(word,key=lambda w:len(w)))
