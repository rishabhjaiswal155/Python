#Program to find the biggest of three numbers 
n1=int(input("Enter First number:"))
n2=int(input("Enter Second number:"))
n3=int(input("Enter Third number:"))
if n1>n2 and n1>n3:
	print("The biggest number is:",n1)
elif n2>n3:
	print("The biggest number is:",n2)
else:
	print("The biggest number is:",n3)
