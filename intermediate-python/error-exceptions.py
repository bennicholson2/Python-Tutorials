#Exceptions and Errors
a = 5
b = 2
c = 3

#SyntaxError - Too many parenthesis, 2 lines of code on the smae line
a = (b + 2))

#TypeError - Adding an int and a string
a = b + '2'

#ImportError - Bringing in an import that does not exist
import error

#NameError - If you call a variable that is not defined
a = b + d

#FileNotFoundError - Is when there is no file directory
f = open('somefile.txt')

#ValueError - Recives the right type but not an appropriate value
import math
math.sqrt(-10)

#IndexError - Try to remove a value that is not existent in a list
list = ['a', 'b', 'c']
list.remove('d')

#KeyError - Is when a key is not a dictionary
dict = {'hello':'world'}
var = dict['goodbye']

#The following is an example of an exception
x = -5
if x<0:
    raise Exception('exception statement')

#Assert - the code has to work or else it will throw an assertion error
assert(c>a)
#To output a statement
assert(c>a), 'this didnt work'

#To see if an argument is working you can do
try:
    c>a
except:
    print('your code does not work')

#If you want to test multiple errors that you are expecting then name errors as variables
try:
    c/0
    a + '5'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else: print('your cod works')

#You can integrate exceptions into classes
class name(Exception):
    pass

#You can also utilise functions, here is an example
class ValueTooHighError(Exception):
    def __init__(self,message,value):
            self.message=message
            self.value = value

def test_value(x):
	if x > 100:
		raise ValueTooHighError('Value is too high')