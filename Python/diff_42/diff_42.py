myInput = int(input("Enter a positive number: "))
x = 42
while myInput < 0:
	myInput = int(input("Error. Enter a positive number: "))
if myInput < x:
	myInput = x - myInput
else: 
	myInput = (myInput-42)*2
print(myInput)
