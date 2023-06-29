#Collections contains - counter, namedtuple, ordereddict, defaultdict, deque

#Counter will count the number of characters or values within an interable type
#To import the tool Counter from collections
from collections import Counter
string = "abbcccddddeeeee"

Counter(string)
counter_obj = Counter(string)

#To get the keys that are in the Counter
counter_obj.keys()

#To get the values that are in the Counter
counter_obj.values()

#To get the most common element that are found in the Counter, the int represents the number of answers you want to see
counter_obj.most_common(2)

#To index into that you can indexing
#[0][0] This would return the most common key
#[0][1] This would return the most common value

#namedtuple will name tuples

#To import namedtuple from collection
from collections import namedtuple

#To name the tuples use this method
Point = namedtuple('Point','x,y,z') #This creates a variable with the type namedtuple
pt = Point(1,-4,10) #Create a new variable with the ability to name the values
#pt.x = 1
#pt.y = -4
#pt.z= 10

#OrderedDict will create a dictionary that is ordered

#To import OrderedDict from collection
from collections import OrderedDict

#To set up an OrderedDict
d = OrderedDict()
d["x"] = "y"
d["a"] = "b"

#defaultdict - Main difference to a normal dictionary is that if the item is not found it returns a default value

#Import defaultdict from collection
from collections import defaultdict

#To create a defaultdict
d = defaultdict(string)
d["x"] = "y"
d["a"] = "b"

#Deque - double ended queue

#Import deque from collection
from collections import deque
d = deque()

#To add an element to the left
d = d.appendleft()

#To add an element to the right
d = d.append()

#To remove an item from the left 
d.popleft()

#To add multiple elements to the left
d.extend([])

#To move the items from left to right by a number times n, use a -n to rotate it to the left
d.rotate(1)