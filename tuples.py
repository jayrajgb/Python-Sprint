### Tuples in Python

# written in round brackets/parentheses --- ()

## Ordered
## Unchangeable
## Duplicates allowed
## Elements can have different datatypes
## Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# x = ("apple", "banana", "cherry")

# n = len(x)

# type(x) is a <class 'tuple'>

# can be made using tuple constructor --- tuple(("apple", "banana", "cherry"))

## remember the comma for one element tuple:

# thistuple = ("apple",)
# print(type(thistuple))

## NOT a tuple, its a string/individual element
# thistuple = ("apple")
# print(type(thistuple)) # <class 'str'>


### Checking

# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#   print("Exists!")


### Updation

# Tuples are unchangeable, meaning that you cannot change, 
# add, or remove items once the tuple is created.

## Tuple ---> Convert to List ---> Modify List ---> Convert to Tuple

# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

## We can add a tuple to tuple --- joining
# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y # joining

## We need to work around with the help list for updation

## Deletion
# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists


### Unpacking Tuples

# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits # should match the length, if not use *

# print(green) # apple
# print(yellow) # banana
# print(red) # cherry

## Using asterisk * ---> retrieves remaining values as list

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red) # ['cherry', 'strawberry', 'raspberry']

# If the asterisk is added to another variable name than the last, 
# Python will assign values to the variable until the number of values left
# matches the number of variables left.

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits

# print(green)
# print(tropic) # ['mango', 'papaya', 'pineapple']
# print(red)


### Looping --- same as lists

### Joining

# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)
# tuple3 = tuple1 + tuple2
# print(tuple3)

# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2
# print(mytuple)


### Tuple Methods

# count() --- occurences
# index() --- first occurence