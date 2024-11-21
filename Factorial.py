#Program to find factorial of given number
def fact(n):
    result=1
    while n>=1:
        result=result*n
        n-=1
    return result
for x in range(1,6):
    print("The factorial of number:{} is {}".format(x,fact(x)))