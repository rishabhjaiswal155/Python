#Program to accept some str from keyboard and print all characters using both postive and negative index.
s=input("Enter some String:")
i=0
for x in s:
	print("The Character at Positive index:{} and at Negative index:{} is {}".format(i,i-len(s),x))
	i=i+1
	