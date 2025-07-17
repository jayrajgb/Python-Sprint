### Sets in Python

# written in curly braces --- {}

## Unordered
## Unchangeable, but you can remove items and add new items.
## Duplicates not allowed
## Elements can have different datatypes (but, True and 1 are same)
## Set is a collection which is unordered, unchangeable, and unindexed. No duplicate members.

# x = ("apple", "banana", "cherry")

# n = len(x)

# type(x) is a <class 'set'>

# can be made using set constructor --- set(("apple", "banana", "cherry"))


### Checking

## You cannot access items in a set by referring to an index or a key.

## use for-in loop
# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#   print(x)

# thisset = {"apple", "banana", "cherry"}
# print("banana" in thisset)


# Once a set is created, you cannot change its items,
# but you can add/remove new items.


### Adding

# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# print(thisset)

## set/iterable into set
# thisset = {"apple", "banana", "cherry"} 
# tropical = {"pineapple", "mango", "papaya"}
# thisset.update(tropical)
# mylist = ["kiwi", "orange"] # any iterable can be added
# thisset.update(mylist)
# print(thisset) 
# {'orange', 'kiwi', 'cherry', 'banana', 'mango', 'papaya', 'apple', 'pineapple'}


### Removing

# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana") # requires a correct/existing value compulsory
# thisset.discard("") # does not produce error on giving incorrect value
# print(thisset)

# using pop() will remove random value 

# use clear() to clear the set

## Deletion
# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset) # this will raise an error because the set no longer exists


### Looping --- only using for in loop

## since, sets are unordered, no index, not iterable, not subscriptable

# thislist = {"apple", "banana", "cherry"}
# for i in range(len(thislist)):
#   print(thislist[i])


### Joining

## union() or | operator keeps all items
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2) # can contain many sets --- set1.union(set2, set3, set4)
# set4 = set1 | set2 # can extend like --- set1 | set2 | set3 | set4
# print(set3, set4)

## union() can join set with any iterable like tuple, list
## | operator only joins sets with sets

## intersection() or & operator keeps only matched items
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.intersection(set2)
# print(set3)

## intersection() can join set with any iterable like tuple, list
## & operator only joins sets with sets

## intersection_update() will keep matched items, and update in the original set
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.intersection_update(set2)
# print(set1)

## difference() or - operator will return new set of values of set1 not present in set2
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 - set2
# print(set3)

## difference_update() will change orignal set

## symmetric_difference() or ^ operator keeps only the elements,
## that are NOT present in both sets

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.symmetric_difference(set2)
# set4 = set1 ^ set2
# print(set3, set4) # {'microsoft', 'banana', 'google', 'cherry'}

# symmetric_difference_update() will change orignal set


### Set Methods

# add() --- adds an element                 clear() --- removes all 
# copy() --- returns a copy                 remove() --- removes specified, error if not
# update() --- updates with any iterable    discard() --- removes specified, no error    
# union() --- union with any iterable       pop() --- random element is popped
# intersection() --- & with iterables       difference() --- difference b/w iterables
# intersection_update() --- &=              difference_update() --- -=
# symmetric_difference() --- ^ operation    symmetric_difference_update() --- ^=
# isdisjoint() --- returns if & exists
# issubset() --- < <=
# issuperset() --- > >=