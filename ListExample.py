#Program to take List items as input and print positive and negative index of each item.
l=[10,20,20,40,50,60,'Rishabh']
i=0
n=len(l)
for x in l:
	print("Item:",x,"is present at positive index:",i,"and at negative index:",i-n)
	i+=1