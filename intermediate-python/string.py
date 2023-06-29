#Strings - ordered, immutable, text representation

#To assign a variable to a string
myString = "string" 
myString = 'string'

#To create a string across multiple lines
str = """Hello
my
name
is"""

#To create a variable based of the location of a character in your string
char = myString[0]

#If you want to create a new variable which is a substring of the original
subString = myString[2:6]

#To reverse the order of your string
myString[::-1]

#To remove any spacing in the string
myString.strip()

#To make all of the items upper case
myString.upper()

#To make all of the items lower case
myString.lower()

#To return a boolean value if your string starts with something
myString.startswith("s")

#To return a boolean value if your string ends with something
myString.endswith("g")

#To find the location of a char in your string
myString.find("t") # will return the location
myString.find("ring") # will return the start of this substring

#To count how many specific characters are in your string
myString.count("t")

#To replace one set of characters with another
myString.replace("str", "b")

#To split your string into a list of individual characters
list = myString.split()

#To combine your list back into a string as before
''.join(list)

#There are three different ways to input variables into your string

#Number 1 - % - You are going use a similar method as programming language C
#You are going to have a variable and use the modulo symbol to intergrate your variable into your string
#%s = string, %d = int, %f = float
var = "world"
myString = "Hello %s" % var

#Number 2 - .format() - Put curly brackets where you want your variable then use the format method
var = "world"
myString = "Hello {}".format(var)

#Number 3 - f strings - Put an f before your string and you can use variables outside
var = "world"
myString = f"Hello {var}"