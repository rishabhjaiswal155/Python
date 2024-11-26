#Function returning another Function

def outer():
	print("outer function execution")
	def inner():
		print("inner function execution")
	print("outer function returning inner function")
	return inner  #outer function returning another function inner
f1=outer() #outer function is called and reference is assigned to f1
f1() #inner function is called when f1() is called
f1()
f1()
