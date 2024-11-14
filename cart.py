#program to add the item in the bill if its price is less than 500 else continue without adding it
cart=[10,20,30,40,500,602,45,69,98]
bill=0
for item in cart:
	if item>=500:
		continue
	bill+=item
	print(item,"is added and bill:",bill)
	