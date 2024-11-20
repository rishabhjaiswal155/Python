#Program to remove duplicates in the list using set().
l=eval(input("Enter some list items:"))
print(l)
s=set(l)
print("After removing duplicates in the list:",list(s))

#using membership operator:
l=eval(input("Enter some list items:"))
print(l)
l1=[]
for x in l:
	if x not in l1:
		l1.append(x)
print("List After removing duplicates:",l1)