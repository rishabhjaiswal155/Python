#Flow Control: Transfer Statements break,continue,pass
#Program to print number from 0-9 if n==7 break
for i in range(10):
	if(i==7):
		break
	print(i)
   
#Program to add the item price in the bill if cart item price is less than 500 and if greater than 500 then break
cart=[10,20,30,40,500,105,205]
bill=0
for item in cart:
    if item>=500:
        break
    bill+=item
    print(item,"is added and bill:",bill)