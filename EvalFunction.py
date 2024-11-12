#eval() function to evaluate some expression.

ex=input("Enter some expression:")
result=eval(ex)
print("The Result of Expression is:",result)

#eval() to take multiple values as input which default is list data type

x=eval(input("Enter items in list:"))
print(type(x))
for x1 in x:print(x1)

