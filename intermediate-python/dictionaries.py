mydict = {"f":"g", "h":"i", "j":"k"}

#Dictionaries are unordered and mutable with key, value pairs

#To get the value of a key
expectg = mydict["f"]

#To add a key and a value to your dictionary
mydict["x"] = "y"

#To override a key with a new value
mydict["x"] = "z"

#To delete a key and its value 
del mydict["x"]
mydict.pop("x")

#To delete the last key/value in the dictionary
mydict.popitem()

#To make a copy of the dictionary that can be mutable
mydict.copy()

#To update your dictionary to contain another dictionary
dictionary = dict(a = "b", b = "c", d="e")
mydict.update(dictionary)

#To return a value based on the key
mydict["a"]

#Using a tuple to create a new key,value in the dictionary
mytuple = (1,2,3)
newdict = {mytuple:6}