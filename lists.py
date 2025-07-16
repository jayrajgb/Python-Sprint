### Lists in Python

# written in square brackets --- []

# Ordered
# Changeable / Mutable
# Duplicates allowed
# Elements can have different datatypes
# List is a collection which is ordered and changeable. Allows duplicate members.

# x = ["apple", "banana", "cherry"]

# n = len(x)

# type(x) is a <class 'list'>

# can be made using list constructor --- list(("apple", "banana", "cherry"))


### Checking

# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Exists!")


### Adding

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist) # ['apple', 'blackcurrant', 'watermelon', 'cherry']

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist) # ['apple', 'watermelon']

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)


### Removing

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop() # last item
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1) # index 1
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist
# print(thislist) # 'thislist' is not defined

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist) # []


### Looping

## Elementwise
# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)

## Indexwise for
# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])

## Indexwise while
# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1

## List comprehension
# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

## List comprehension example:
# Based on a list of fruits, you want a new list, 
# containing only the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for statement 
# with a conditional test inside:

# Traditional:
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
# print(newlist)

# New:
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)

# newlist = [expression for item in iterable if condition == True]

# newlist = [x for x in fruits]

# newlist = [x for x in range(10) if x < 5]

# newlist = [x.upper() for x in fruits]

# newlist = [x if x != "banana" else "orange" for x in fruits] 
# "Return the item if it is not banana, if it is banana return orange".


### Sorting

# nums = [100, 50, 65, 82, 23]
# nums.sort()
# nums.sort(reverse = True)
# print(nums)

# Comparator!!!
# def nearfifty(n):
#   return abs(n - 50)
# nums = [100, 50, 65, 82, 23]
# nums.sort(key = nearfifty) 
# # [50, 0, 15, 32, 27] ---> [0, 15, 27, 32, 50] ---> indexes: [1, 2, 4, 3, 0]
# # [50, 65, 23, 82, 100]
# print(nums)

# By default the sort() method is case sensitive, 
# resulting in all capital letters being sorted before lower case letters:
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist) # ['Kiwi', 'Orange', 'banana', 'cherry']
# thislist.sort(key = str.lower)
# print(thislist) # ['banana', 'cherry', 'Kiwi', 'Orange']

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)


### Copying

# list1 = ["apple", "banana", "cherry"]

# list2 = list1.copy() # copy method

# list3 = list(list1) # list constructor

# list4 = list1[:] # slice operator

# list5 = list1 # is not true, list5 is just a reference to list1, list5 is not a copied list
# list5[0] = "kiwi"
# print("List 1:", list1) # list1 is changed to ['kiwi', 'banana', 'cherry']


### Joining 

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2 # addition + operator

# for x in list2:     # looping
#   list1.append(x)

# list1.extend(list2) # extend method


### List Methods

# append() --- added to the end               insert() --- added at specified index
# clear() --- empty list                      pop() --- removes from specified, else last
# copy() --- creates copy                     remove() --- specified value removed
# count() --- occurences                      reverse() --- reverse order
# extend() --- can add iterable to list       sort() --- sorted order
# index() --- first occurence
