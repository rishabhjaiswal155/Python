#Concept of Decorator Chaining

def decor1(func):
    def inner(name):
        print("decor1() function executing")
        func(name)
    return inner

def decor2(func):
    def inner(name):
        print("decor2() function executing")
        func(name)
    return inner
    
@decor2	
@decor1 #Flow control in decorator chaining is from top to bottom
def wish(name):
	print("Hello",name,"Good Morning")

wish("Rishabh")


#Example of Decorator chaining

def decor3(func):
    def inner():
        print("decor3() function executing")
        x=func()
        return x*x
    return inner
    
def decor4(func):
    def inner():
        print("decor4() function executing")
        x=func()
        return 2*x
    return inner

@decor4
@decor3
def num():
    return 10

print(num())