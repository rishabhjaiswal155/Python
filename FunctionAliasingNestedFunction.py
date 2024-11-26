#Function Aliasing in Python (Every thing in python is object including Function also)
def wish(name):
	print("Hello!Good Morning",name)
greeting=wish
print(id(greeting),id(wish)) #same memory address as both function name pointing to same object
greeting("Rishabh")
wish("Vishal")
del wish
greeting("Amol")

#Nested Functions
def outer():
    print("outer Function execution started....")
    def inner():
        print("inner function execution started....")
    inner()
    inner()
    inner()
outer()

#example of Nested Functions

def f1():
    def inner(a,b):
        print("The sum of two numbers is:",a+b)
        print("The Average of two numbers is:",(a+b)/2)
    inner(10,20)
    inner(25,31)
f1()
