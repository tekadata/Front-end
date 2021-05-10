import sys
# Importer le module sys(tem)

myList = sys.argv[1:]
if myList[0] == 'fly':
    print("I'm a bird!")
elif myList[0] == 'swim':
    print("I'm a shark!")
