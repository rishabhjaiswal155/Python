#identity operator is,id,is not
a=10
b=10
print(a is b)
print(a is not b)
print(id(a))
print(id(b))


#Difference between reference equality using identity operator 'is' and content equality '=='
a=10
b=11
print("Content equality:",a==b)#false
print("reference equality:",a is b)#false 