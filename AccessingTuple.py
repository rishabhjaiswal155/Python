#Accessing Tuple elements
t=(10,20,30,40,50,'Rishabh')
print(t[0]) #accessing tuple elements using positive index
print(t[-1]) #accessing tuple elements using negative index
print(t[::]) #accessing tuple elements using slice operator
print(t[0:5:1])
print(t[-1:-5:-1])

# Tuple using Mathematical operator +,*
t1=10,20,30,50
t2=(25,65,98,78)
t3=t1+t2
print(t3)
print(t1*3)

#Tuple immutability
t=(10,20,50,'Rishabh','Jaiswal')
t[1]=256 #It gives error as tuple is immutable.
