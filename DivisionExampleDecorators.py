#Division Example of Function Decorators

def smartdivision(func):
    def inner(a,b):
        if b==0:
            print("ZeroDivisionError: you cannot provide denominator value as zero")
        else:
            return func(a,b)
    return inner

@smartdivision
def division(a,b):
    return a/b
    
print(division(10,2))
print(division(15,2))
print(division(10,0))

    