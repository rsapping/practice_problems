myList=[
  [150, 6, 240, 129, 168, 346, 218, 168, 309, 242, 26, 327],
  [150, 6, 240, 129, 168, 346, 218, 168, 309, 242, 26, 327],
  [98, 275, 315, 389, 270, 2, 172, 100, 151, 41, 217, 176],
  [98, 275, 315, 389, 270, 2, 172, 100, 151, 41, 217, 176],
  [267, 5, 324, 344, 134, 122, 229, 196, 225, 280, 200, 274],
  [267, 5, 324, 344, 134, 122, 229, 196, 225, 280, 200, 274],
  [155, 320, 8, 215, 273, 291, 174, 165, 279, 26, 327, 214],
  [155, 320, 8, 215, 273, 291, 174, 165, 279, 26, 327, 214],
  [207, 91, 121, 46, 125, 247, 303, 387, 214, 249, 97, 316]
]
'''
for i in range(0,len(myList)):
    for j in range(0,len(myList[i])):
        print(myList[i][j])
'''

m=len(myList)
n=len(myList[0])
t=0
b=m-1
l=0
r=n-1
dirr = 0

while(t<=b and l<=r):
    
    if(dirr==0):
        print("0 --" + str(l))
        for i in range(l,r+1):
            print(myList[t][i])
        t+=1
        dirr+=1
    elif(dirr==1):
        print("1 --"+str(t))
        for j in range(t,b+1):
            print(myList[j][r])
        r-=1
        dirr+=1
    elif(dirr==2):
        print("2 --"+str(r))
        for k in range(r, l-1,-1):
            print(myList[b][k])
        b-=1
        dirr+=1
    
    elif(dirr==3):
        print("3 --"+ str(l))
        for o in range(b, t-1, -1):
            print(myList[o][l])
        print("value of l before " + str(l))
        l+=1
        print("value of l after " + str(l))
        dirr=0 

