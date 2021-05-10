s = input("Enter a sentence: ")
if len(s) != 0:
    s = s[:-1]+s[-1].upper()
    print(s)
