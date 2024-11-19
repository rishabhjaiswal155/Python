#Program to take a tuple of numbers from keyboard and print sum,average.
t=eval(input("Enter some numbers in tuple:"))
print(t)
l=len(t)
sum=0
for x in t:
	sum+=x
print("The sum=",sum)
print("The Average=",sum/l)

