
myList = [10,20,30,40,50,60,70,80,90,100,110]
for i in range(0,len(myList)//2):
    print(str(myList[i]) + " "+ str(myList[~i]))
    #print(str(i) + " "+ str(~i))
