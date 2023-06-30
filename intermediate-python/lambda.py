#lambda is best done when you are trying to use a function for one case
#The layout of a lambda var = list(argument:expression)

#The following is an example of a basic lambda function
#This is how you would sort these points in the x axis (default)
Points = [(1,2), (15,1), (5,-1), (10,4)]
Points_sorted = sorted(Points)

#However, if you want to sort the list in the y axis you must use a lambda function
Points_sorted_y = sorted(Points, key = lambda x: x[1])

#If you want to sort the list by adding the two numbers you can do that too!
Points_sorted_sum = sorted(Points, key = lambda x: x[0] + x[1])

#The map method has the following layout var = map(lambda x: argument, iterable (such as a tuple))
#Basically you can make this apply for every value within an iterable set of data
#The following 2 examples multiply the original values by 2

#This will replace the original x values with x multiplied by 2
A = [1,2,3,4,5]
B = map(lambda x:2*x, A) 

#You can perform the same task using a for loop
C = [x*2 for x in A]

#You can combine the filter function with lambda to return values that have a certain argument
#The layout is filter(function, sequence)
#The following 2 examples return values that are divisible by 2

#filter, lambda example (must convert to list to print)
A = [1,2,3,4,5,6]
B = filter(lambda x:x%2==0, A)
print(B)

#for loop example (must convert to list to print)
C = (x for x in A if x%2==0)
print(C)

#reduce function using lambda
#The layout is var = reduce(lambda x,y(must have 2): x*y,a)
#The following example is a much simpler way of doing the fibonacci sequence

from functools import reduce
product_a = reduce(lambda x,y: x*y,A)