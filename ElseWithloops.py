#else with for,while etc
for i in range(10):
    if i==5:
        print("Nthing to break")#break if here break is executed then else part will not execute
    print(i)
else:
    print("Congrats!!You have completely executed the loop...")