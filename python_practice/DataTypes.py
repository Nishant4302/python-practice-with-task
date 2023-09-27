# Built-in Data Types

# ext Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

x = "Hello World"	#str	
x = 20 #int	
x = 20.5    #	float	
x = 1j	#complex	
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	#range	
x = {"name" : "John", "age" : 36}	#dict	
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	#bool	
x = b"Hello"	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview	
x = None	#NoneType



#-------------------------------------------------- Python Numbers-----------------------------------------

#   int
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
# without point number are int number
z=5
x=4
x=-5

#   float
# Float, or "floating point number" is a number, positive or negative, containing one or more decimals
# point number are call float number
x=5.4
y=-5.789

#   complex
# Complex numbers are written with a "j" as the imaginary part
x = 3+5j
y = 5j
z = -5j


# -----------------------------------------Python Casting---------------------------------------------------- 
# in python casing means to change data type like int to convert to float // float to convert to int // int to convert to str
# in case string all element is number then you can change to in toint otherwise you got a error
# and another use to casting that is There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types   

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3")# z will be 3
x=3.0
y= int(x) # y will be 3




# ----------------------------------------------------Python Strings-------------------------------------------

# Assign String to a Variable
a = "Hello"
print(a)

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# access to string using index number

a = "Hello, World!"
print(a[1])

# Length
# The len() function returns the length of a string:
print(len(a))

# Check String
txt = "The best things in life are free!"
print("free" in txt) # return True

txt = "The best things in life are free!"
print("expensive" not in txt) # return True

# Slicing

# You can return a range of characters by using the slice syntax.

# Specify the start index and the end index, separated by a colon, to return a part of the string

# Slice From the Start
b="Python Programming Language"
c= b[:5]    ## c will be Ptyhon

# Slice To the End
d= b[-6:]     ### d will be nguage

# Negative Indexing
e= b[-5:-2]   #### e will be gua

print(c, d, e)

# Python - Modify Strings
# Upper Case
print(a.upper())

# Lower Case
print(a.lower())
# Remove Whitespace
print(a.strip()) # returns "Hello, World!"

# Replace String
print(a.replace("H", "J"))

# Split String

print(a.split(","))


# Python - Format - Strings

# String Format

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


# -----------------------------------------------Python Booleans---------------------------------------------

# this is return True and False 
print(10 > 9)
print(10 == 9)
print(10 < 9)

#---------------------------------------------- Python Lists -----------------------------------------------
mylist = ["apple", "banana", "cherry"]

# Lists are used to store multiple items in a single variable.
# Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"

# Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Append Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Extend List

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Remove Specified Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


thislist = ["apple", "banana", "cherry"]
del thislist

# Clear the List
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list



#----------------------------------------------Python Tuples-------------------------------------------------
# Tuples are used to store multiple items in a single variable.

# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

# A tuple is a collection which is ordered and unchangeable.

# Tuples are written with round brackets.
x = ("apple", "banana", "cherry")

# Change Tuple Values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# add Items

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# Remove Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# --------------------------------------------Python Sets--------------------------------------------------

# Sets are used to store multiple items in a single variable.

# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

# A set is a collection which is unordered, unchangeable*, and unindexed

thisset = {"apple", "banana", "cherry"}
print(thisset)
print(type(thisset))

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# Add Items
thisset.add("orange")

# Add Sets
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

# Add Any Iterable

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

# Remove Item
thisset.remove("banana")

# Join Two Sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
set1.update(set2)


# Method	Description
# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others

# ------------------------------------- Python Dictionaries---------------------------------------------

# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])
x = thisdict.get("model")
x = thisdict.keys()
x = thisdict.values()
x = thisdict.items()

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

# # clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary