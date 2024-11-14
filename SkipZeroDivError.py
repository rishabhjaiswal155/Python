#Program to divide a number by item in list if it is not zero else skip that using continue
list=[10,20,30,40,0,50,0,60]
for item in list:
    if item==0:
        print("Hey,How can you divide a number by 0....Gone Mad!!!")
        continue
    print("100/{}={}".format(item,100/item))
    