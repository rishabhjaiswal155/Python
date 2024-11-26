#filter function in lambda(Anonymous function) and normal function

#Program to check if the given number in sequence is even or not using filter() in Normal Function.

def iseven(n):
	if n%2==0:
		return True
	else:
		return False
l1=[2,3,5,7,89,14,25,36,51]
l2=list(filter(iseven,l1))
print("The List of even numbers is",l2)


#Program to check if the given number in sequence is even or odd using filter() in lambda Function.

l1=[2,3,5,7,89,14,25,36,51]
l2=list(filter(lambda n:n%2==0,l1))
l3=list(filter(lambda n:n%2!=0,l1))
print("The List of Even number is:",l2)
print("The List of Odd number is:",l3)