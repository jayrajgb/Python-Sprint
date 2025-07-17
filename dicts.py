### Dictionaries in Python

# written in curly braces with key-value pairs --- { key : value }

## Ordered - since 3.7 update
## Changeable
## Duplicates not allowed
## Elements can have different datatypes
## Dictionary is a collection which is ordered and changeable. No duplicate members.

# x = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }

# n = len(x)

# type(x) is a <class 'dict'>

# can be made using set constructor --- dict(name = "John", age = 36, country = "Norway")


### Accessing

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# x = thisdict["model"] # Mustang
# x = thisdict.get("year") # 1964

## keys() returns a list of keys --- just a view
# print(thisdict.keys()) # dict_keys(['brand', 'model', 'year'])

## values() returns a list of values --- just a view
# print(thisdict.values()) # dict_values(['Ford', 'Mustang', 1964])

## items() returns a list of tuples --- just a view
# print(thisdict.items()) # dict_items([('brand','Ford'),('model','Mustang'),('year',1964)])


### Checking

# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")


### Change values

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["year"] = 2018 # year: 2018
# thisdict.update({"year": 2020}) # year: 2020


### Adding

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# thisdict.update({"sunroof": True})
# print(thisdict)


### Removing

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# thisdict.popitem() # removes last item
# thisdict.clear() # removes all items
# del thisdict["model"]
# del thisdict # complete delete


### Looping

## Keys printing
# for x in thisdict:
#   print(x) # keys printed

# for x in thisdict.keys():
#   print(x)


## Values printing
# for x in thisdict:
#   print(thisdict[x]) # values printed

# for x in thisdict.values():
#   print(x)


## Both at the same time
# for x, y in thisdict.items():
#   print(x, y)


### Copying

# dict2 = dict1 # is just a reference

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict1 = thisdict.copy()
# mydict2 = dict(thisdict)


### Nested dictionaries
# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
#   # child1, child2, child3 are individual dictionaries
# }



