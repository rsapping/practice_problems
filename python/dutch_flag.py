
def dutch_flag(pivot, myList):
   #print(type(myList))
   #print(type(pivot))
   less = []
   higher = []
   middle = []
   pivot = myList[pivot]
   print("privot is " + str(pivot))
   
   #O(n) time
   #O(n) space, with n being the length of myList
   for item in myList:
       if(item > pivot):
           higher.append(item)
       elif(item == pivot):
           middle.append(item)
       else:
           less.append(item)

   print(less+middle+higher)

def main():
    myList = [0,1,2,3,2,1,0,3]
    pivot = 4
    dutch_flag(pivot, myList)

main()

