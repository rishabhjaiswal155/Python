#Type of Variables i.e Global and Local variables
a=100 #Here a is Global variable
def f1():
	a=120 #Here a is local variable
	print("f1():",a)
def f2():
	print("f2():",a)
f1()
f2()

#global keyword in python
a=100 #Here a is Global variable
def f1():
    global a
    a=120 #Here a which is global variable is modified
    print("f1():",a)
def f2():
	print("f2():",a)
f1()
f2()

#globals() function in python

def f1():
	global a
	a=120 
	print("f1():",a)
def f2():
	print("f2():",globals()['a'])
f1()
f2()