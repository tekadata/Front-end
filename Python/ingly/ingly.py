sInput = input("Give us a word: ")
if sInput[-3:] == "ing":
    sInput = sInput+"ly"
else:
    sInput = sInput+"ing"
print(sInput)
