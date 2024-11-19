#Tuple data Structure 
#Tuple creation

t=() #creating empty tuple
print(type(t),t)

t=(10,) #creating single value tuple
print(type(t))
print(t)

t=10,20,30,40 #creating tuple without parenthesis
t1=(10,20,30,40) #with parenthesis
print(type(t),type(t1))
print(t,t1)

list=[10,20,30,40]
t=tuple(list) #creating tuple from list using tuple()
print(type(t),t)

t=tuple(range(10)) #creating tuple from range sequence using tuple()
print(type(t),t)

t=tuple('Rishabh') #creating tuple from string using tuple()
print(type(t),t)

