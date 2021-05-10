max = int(input ("How many char max? "))
myInput = input ("I will repeat: ")
myInputsLen = len(myInput)
print (myInput)
while myInputsLen<max:
	myInput = input ("I will repeat: ")
	myInputsLen = myInputsLen + len(myInput)
	print (myInput)
