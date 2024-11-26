#Lambda functions (lambda input:Expression)
#Where lambda is keyword in python
#Program to print the square of given number using lambda

f=lambda n:n*n
print("The square of given number is:",f(4))

f=lambda a,b:a+b
print("The sum of two numbers is:",f(10,20))

f=lambda a,b:a if a>b else b
print("The greater number amongst two is:",f(11,23))

