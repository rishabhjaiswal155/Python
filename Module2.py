#The special variable __name__

def f1():
	if __name__=='__main__':
		print("The code executed directly as a Program")
	else:
		print("The code executed indirectly as a module from some other program")
		print("The value of __name__ is:",__name__)
f1()		
	