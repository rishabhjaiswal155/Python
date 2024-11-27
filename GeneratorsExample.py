#Program to Generate first n number using Generator

def genfirstn(n):
	i=1
	while i<=n:
		yield i
		i=i+1
g=genfirstn(10)
print("The First n numbers are:")
for x in g:
	print(x,end=" ")
print()
	

#Program to generate Fibonacci numbers upto 100 using Generator

def fib():
	a,b=0,1
	while True:
		yield a
		a,b=b,a+b
values=fib()
print("The Fibonacci numbers upto 100:")
for x in values:
	if x>100:
		break
	print(x,end=" ")