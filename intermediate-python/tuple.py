mytuple = (1,2,3,4,5)
mylist = [6,7,8,9,10]

#tuples are similar to lists but they allow duplicates and cannot be modified

#To get the location of an item in a tuple
mytuple.index()

#To convert a list to a tuple
list = tuple(list)

#To convert a tuple to a list
tuple = list(tuple)

#To assign variables to values in the tuple
Ben, Nev, Gav, Cai, Pat = tuple
var1, var2, var3, var4, var5 = tuple

#To assign values in tuple to variables
i1, *i2, i3 = tuple
i1 = 1, i2 = 2,3,4, i3 = 5