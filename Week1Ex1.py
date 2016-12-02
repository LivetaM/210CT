import random
def shuffle(givenList):
    new_List = []
    list_Index = len(givenList) - 1 #length of the array that we have got

    if len(givenList) < 2: #if given array length is smaller then 2, it will print out the message
        print ("This array is too short to shuffle, please enter more integers!")
    while list_Index != 0:
        newIndex = random.randint(0,len(givenList)-1)#randomly chosen integers to use as new list index
        givenList[newIndex],givenList[list_Index] = givenList[list_Index],givenList[newIndex] #swaps list integers using list index and newIndex that we found
        list_Index = list_Index - 1
    return (givenList)
        
print (shuffle([5,3,8,6,1,9,2,7])) #prints out the new list

