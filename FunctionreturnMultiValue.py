#Program to return multiple values from function
def calci(a,b):
	add=a+b
	sub=a-b
	mult=a*b
	div=a/b
	return add,sub,mult,div
a,b,c,d=calci(10,5)
print("The addition is:",a)
print("The substraction is:",b)
print("The multiplication is:",c)
print("The division is:",d)