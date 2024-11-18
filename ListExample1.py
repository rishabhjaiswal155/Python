#Program to add all elements to list upto 100 which are divisible by 10.
l=[]
for x in range(101):
	if x%10==0:
		l.append(x)
print(l)