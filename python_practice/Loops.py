# -------------------------------Python Loops------------------------------------------------------------


# Python has two primitive loop commands:

# while loops
# for loops



# ------------------------------------------The while Loop-----------------------------------------------
# With the while loop we can execute a set of statements as long as a condition is true.
i = 1
while i < 6:
  print(i)
  i += 1


# The break Statement
# break statement use to stop loop

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# The continue Statement

# With the continue statement we can stop the current iteration, and continue with the next:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")




# ------------------------------------Python For Loops------------------------------------------------

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#  range() Function
for x in range(6):
  print(x)

for x in range(2, 6):
  print(x)

for x in range(2, 30, 3):
  print(x)

# Else in For Loop

for x in [0, 1, 2]:
  print (x)
else:
  print ("This will only execute when loop is ended.")

# pass Statement

for x in [0, 1, 2]:
  pass