#map() in Lambda

#Program to double the number given in the sequence using map() in normal function

def double(n):
	return 2*n
l1=[0,1,2,4,5,10,60,100]
l2=list(map(double,l1))
print("The double of given sequence using normal function is:",l2)


#Program to double the number given in the sequence using map() in lambda function

l1=[0,1,2,4,5,10,60,100]
l2=list(map(lambda n:2*n,l1))
print("The double of given sequence using lambda is:",l2)

