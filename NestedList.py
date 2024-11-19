#Nested List
l=[[10,20,30],[40,50,60],[70,80,90]]
print(l)
print("Elements of List row wise:")
for r in l:
    print(r)
print("Elements of List in matrix style:")
for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[i][j],end=' ')
    print()

