myList = [1,2,3,4,5,6,7,8,9]

#To find the length of the list
len(myList)

#To add a value to the list
myList.append(10)

#To add a value to the list at a location
myList.insert(3,3.5)

#To remove the last item in the list / remove a certain item
myList.pop()
myList.pop(3)

#To sort the list in a sequence from smallest to largest.
myList.sort()

#To sort the list in a sequence from smallest to largest while making new list
myList.sorted()

#To make a copy of the list
myList.copy()

#create a new list between certain index elements
myList[0:5]

#create a new list between certain index elements with a step
myList[0:9:2]

#create a new array by doing something to the original
newList = [i*i for i in myList]