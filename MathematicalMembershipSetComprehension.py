#Mathematical Operations in set

s1={10,20,30,40,50,80,90}
s2={10,20,30,100,110,120}
print(s1,s2)
print("After union():",s1.union(s2))
print("After |:",s1|s2)
print("After intersection():",s1.intersection(s2))
print("After &:",s1&s2)
print("After difference():",s1.difference(s2))
print("After -:",s1-s2)
print("After symmetric_difference():",s1.symmetric_difference(s2))
print("After ^:",s1^s2)

#Membership operator in,not in
s1={10,20,30,40,50}
print(20 in s1)
print(25 in s1)
print(45 not in s1)

#set comprehension
s1={x*x for x in range(1,11) if (x*x)%2!=0}
print(s1)



