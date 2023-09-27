# Variables
# Variables are containers for storing data values

# Creating Variables
# Python has no command for declaring a variable.

# A variable is created the moment you first assign a value to it.

x = 5 # 5 assigns in x
y = "John" 
print(x)
print(y)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.

# Casting
# If you want to specify the data type of a variable, this can be done with casting.


x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#how to get type

print(type(x))
print(type(y))
print(type(z))


# Single or Double Quotes

x='John'
x="John"
# this is same both are 

# Variable names are case-sensitive.
a = 4
A = "Sally"
print(a,A)
#A will not overwrite a

x, y, z = "Orange", "Banana", "Cherry" # Assign Multiple Variables


# Global Variables
# assign to out of the functions

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# local Variables
#  assign to  in the functions
def myfunc():
  locvar = "Python is awesome."

myfunc()   #locvar only exist inside function and it won't affect outside