myset = {1,2,3}
#Sets are unordered, mutable and contain no duplicates

#If you were to try and make a set with duplicate elements
myset_duplicate = {1,2,3,1,2} #it will print the same as myset

#To print a string with individual letters
myset_string = set("string")

#To add an element to the set
myset.add()

#To remove an element that is in the set, if it is not in the set it will throw an error.
myset.remove()

#To remove an element that is found in the set and will not throw an error if it is not in the set.
myset.discard()

#To remove all elements from the list
myset.clear()

#To get rid of the first element in the list
myset.pop()

set1 = {1,2,3,7,8,9}
set2 = {2,4,6,8,10}

#Will create a new set combining elements from two different sets
set1.union(set2)

#Will create a new set with elements that are found in both set1 and set2
set1.intersection(set2)

#Will create a new set where the only the elements that are not found in set2 but are found in set1 are printed
set1.difference(set2)

#Will create a new set with the elements that are symmetrical set1 and set2
set1.symmetric_difference(set2)

#Will create a new set where set2 is added to set1
set1.update(set2)

#Will create a new set where the elements that are mutually exclusive from set1 and set2
set1.symmetric_difference(set2)

#Will update the set with only the elements that are found in set1 and set2
set1.intersection_update(set2)

#Will return true if all elements in set2 are within set1
set1.issubset(set2)

#Will return true if no elements from set1 are within set2
set1.disjoint(set2)

#To make an immutable set 
frozen_set = frozenset([1,2,3,4])