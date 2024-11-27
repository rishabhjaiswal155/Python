#Difference between List Comprehension/other collections and Generator
#Other Collections or List stores the object into the memory while Generator does not stores into memory
#So Generator is better choice in terms of Performance

l=(x*x for x in range(1000))
print(type(l))
for x in l:
    print(x)

#Generator Example

def mygen():
    yield 'A'
    yield 'B'
    yield 'C'
    yield 'D'
s=mygen()
print(type(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))

#Generator Example

def countdown(num):
    while num>0:
        yield num
        num=num-1
c=countdown(10)
print(type(c))
for x in c:
    print(x)