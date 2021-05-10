s = input("Enter a sentence: ")
sd = ""
if len(s) != 0:
    for c in s:
        if c in "nspl":
            sd = sd+c*2
        else:
            sd = sd+c
print(sd)
