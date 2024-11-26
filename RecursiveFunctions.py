#Recursive functions
#Program to find the factorial of given number using recursion

def factorial(n):
	if n==0:
		result=1
	else:
		result=n*factorial(n-1)
	return result
print("The factorial of {} is :{}".format(0,factorial(0)))
print("The factorial of {} is :{}".format(5,factorial(5)))
print("The factorial of {} is :{}".format(3,factorial(3)))