#map() for mutiple sequences in lambda

l1=[1,2,3,4,5]
l2=[2,3,6,4,5]
l=list(map(lambda x,y:x*y,l1,l2))
print(l)

#reduce() in functools module
from functools import *
l=[10,20,45,58,98]
result=reduce(lambda x,y:x+y,l)
print("reducing sequnce l into single value:",result)
