#Program to take input one character from keyboard and check whether it is alphanumeric,alpha,digit,space,lower,upper or nonspace special character

c=input("Enter any one character:")
if c.isalnum():
	print("charcter",c,"is alphanumeric")
	if c.isalpha():
		print("charcter",c,"is alpha")
		if c.isupper():
			print("character",c,"is upper")
		else:
			print("charcter",c,"is lower")
	elif c.isdigit():
		print("character",c,"is digit")
elif c.isspace():
	print("character",c,"is space")
else:
	print("character",c,"is non space special character")
