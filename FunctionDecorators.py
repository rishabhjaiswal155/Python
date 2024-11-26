#Function Decorators
#using annotation

def decor(func):
	def inner(name):
		if name=='Pranav':
			print("Hello Pranav Bad Morning")
		else:
			func(name)
	return inner

@decor
def wish(name):
	print("Hello",name,"Good Morning")

wish("Rishabh")
wish("Pranav")
wish("Vishal")

#using without annotation

def decor(func):
	def inner(name):
		if name=='Pranav':
			print("Hello Pranav Bad Morning")
		else:
			func(name)
	return inner

decorfunction=decor(wish) #use instead of @ annotation

def wish(name):
	print("Hello",name,"Good Morning")

wish("Rishabh")
wish("Pranav")
wish("Vishal")
decorfunction("Pranav")