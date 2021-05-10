s = input("Give me your email: ")
iAt = s.find('@')
iDot = s[iAt:].find('.')
if s:
    if iAt > 0 and iDot > 0:
        print(s[iAt+1:iAt+iDot])
