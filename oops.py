### OOPs in Python

### Keywords
# self --- used to reference current instance of the class, and access methods of the class.
# __init__ --- is a constructor

### Classes and Objects
## Example
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)


### __str__() function --- decides what to return when object is created.

## without __str__()
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)
# print(p1) # <__main__.Person object at 0x15039e602100>

## with __str__()
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def __str__(self):
#     return f"{self.name}({self.age})"    

# p1 = Person("John", 36)
# print(p1) # John(36)


### Object Methods --- object can consists of methods, defined in the class
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

#   def intro(abc): # self can be named anything, just it needs to be first parameter.
#     print("Hello my name is " + abc.name)

# p1 = Person("John", 36)
# p1.myfunc()
# p1.intro()


## modifying properties of p1 object
# p1.age = 16 # age updated for p1
# del p1.age # property age of p1 is removed
# del p1 # p1 object deleted


#############################################################################################
#############################################################################################


### Inheritance
## Parent Class --- Base Class
## Child Class --- Derived Class

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

## Use the Person class to create an object, and then execute the printname method:
# x = Person("John", "Doe")
# x.printname()

## Use the pass keyword when you do not want to add any other new properties or methods to the class.
# class Student(Person): 
#   pass
# x = Student("Mike", "Olsen")
# x.printname()

## The child's __init__() function overrides the inheritance of the parent's __init__() function.

## but we can add the properties of parent's constructor by adding under child's constructor
# class Child(Parent):
#   def __init__(self, fname, lname):
#     Parent.__init__(self, fname, lname)

## else use super() to do the same
# class Child(Parent):
#   def __init__(self, fname, lname):
#     super().__init__(fname, lname)


#############################################################################################
#############################################################################################


### Polymorphism

