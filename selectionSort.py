
def selectionSort_space(myList):
    new_list = []

    for j in range(0,len(myList)):
        temp = 9999
        index = 999
        for i in range(len(myList)):
            if myList[i] < temp:
                temp = myList[i]
                index=i
        new_list.append(myList[index])
        myList[index]=9999
    return new_list

def selectionSort_inSplace(myList):
    for j in range(0,len(myList)):
        temp = 9999
        index = 999
        for i in range(j,len(myList)):
            if myList[i] < temp:
                temp = myList[i]
                index=i
        temp2 = myList[j]
        myList[j] = myList[index]
        myList[index] = temp2
    return myList

def main():

    #Uses O(n^2) time and O(n) space
    myList = [2,3,6,8,9,1,4,5,10,7]
    print(myList)
    print(selectionSort_space(myList))

    #Uses O(n^2) time and O(1) space
    myList = [2,3,6,8,9,1,4,5,10,7]
    print(selectionSort_inSplace(myList))

main()
