#Itertools - product, permutations, combinations, accumulate, count, cycle

#To import all of these:
from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, count, cycle, repeat

#Product - multiplies each value in one list by each value in another list
list1 = ["a","b"]
list2 = ["c", "d"]
prod = product(list1, list2)

#Permutation - return all different orders of inputs
list3 = ["x", "y", "z"]
perm = permutations(list3)

#Combinations - return all the different ways that the list items can be displayed, the second value being the length of list
comb = combinations(list3,2)

#Combinations_with_replacement will do the same but allow duplicate values
comb_dup = combinations_with_replacement(list3,2)

#Accumulate - will add the number before and the number before that together
accum = accumulate(list3)

#Count - will make an infinite loop increase by natural numbers, here is an example counting from 1-15
counter = count(1)
for x in counter:
    print(x)
    if x==15:
        break

#Cycle - Will repeat the sequence and return it back, this will print out 10 different values
cyc = cycle(list3)
for i in range(10):
    print(next(cyc))