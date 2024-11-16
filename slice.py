#Slice Operator in str
'''
s[begin:end:step] if step is positive then forward direction,if step is negative then backward direction
In forward direction,Default values are:
begin=0,end=end-1,step=1
In Backward direction,Default values are:
begin=-1,end=-(len(str)+1),step=-1
'''

s="Rishabh"
print(s[0:7:1]) #Rishabh
print(s[0:-6:-1]) # ''
print(s[2:-5:1]) # ''
print(s[:0:-1]) #hbahsi
print(s[-1::-1]) #hbahsiR
print(s[-5:0:-9]) # 's'
print(s[2:-1:-1]) # ''