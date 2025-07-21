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


### Types of Inheritance

## Single Inheritance

# # Base class
# class Parent:
#     def func1(self):
#         print("This function is in parent class.")

# # Derived class
# class Child(Parent):
#     def func2(self):
#         print("This function is in child class.")

# # Driver code
# obj = Child()
# obj.func1()
# obj.func2()


## Multilevel Inheritance

# # Base class
# class Grandfather:
#     def __init__(self, grandfathername):
#         self.grandfathername = grandfathername

# # Intermediate class
# class Father(Grandfather):
#     def __init__(self, fathername, grandfathername):
#         self.fathername = fathername
#         # Call the constructor of Grandfather
#         Grandfather.__init__(self, grandfathername)

# # Derived class
# class Son(Father):
#     def __init__(self, sonname, fathername, grandfathername):
#         self.sonname = sonname
#         # Call the constructor of Father
#         Father.__init__(self, fathername, grandfathername)

#     def print_name(self):
#         print('Grandfather name :', self.grandfathername)
#         print('Father name :', self.fathername)
#         print('Son name :', self.sonname)

# # Driver code
# s1 = Son('Prince', 'Rampal', 'Lal mani')
# print(s1.grandfathername)
# s1.print_name()


## Hierarchical Inheritance

# # Base class
# class Parent:
#     def func1(self):
#         print("This function is in parent class.")

# # Derived class 1
# class Child1(Parent):
#     def func2(self):
#         print("This function is in child 1.")

# # Derived class 2
# class Child2(Parent):
#     def func3(self):
#         print("This function is in child 2.")

# # Driver code
# object1 = Child1()
# object2 = Child2()

# object1.func1()
# object1.func2()
# object2.func1()
# object2.func3()


## Multiple Inheritance

# # Base class 1
# class Mother:
#     mothername = ""

#     def mother(self):
#         print(self.mothername)

# # Base class 2
# class Father:
#     fathername = ""

#     def father(self):
#         print(self.fathername)

# # Derived class
# class Son(Mother, Father):
#     def parents(self):
#         print("Father :", self.fathername)
#         print("Mother :", self.mothername)

# # Driver code
# s1 = Son()
# s1.fathername = "RAM"
# s1.mothername = "SITA"
# s1.parents()


## Diamond Problem 
# to resolve the ambiguity, when inheriting, 
# the class where that method is implemented first, will get executed.

## Scenario 1: Where method is overridden in both classes.
# class Class1:
#     def m(self):
#         print("In Class1") 
      
# class Class2(Class1):
#     def m(self):
#         print("In Class2")

# class Class3(Class1):
#     def m(self):
#         print("In Class3")  
       
# class Class4(Class2, Class3):
#     pass   
    
# obj = Class4()
# obj.m() # In Class2 (if we inherited, Class3, Class2, then it would be In Class3)

## Scenario 2: Where method is overridden in one of the classes.
# class Class1:
#     def m(self):
#         print("In Class1") 
      
# class Class2(Class1):
#     pass

# class Class3(Class1):
#     def m(self):
#         print("In Class3")    
     
# class Class4(Class2, Class3):
#     pass       

# obj = Class4()
# obj.m()


## Scenario 3: Where method is defined in class itself.
# class Class1:
#     def m(self):
#         print("In Class1") 
      
# class Class2(Class1):
#     def m(self):
#         print("In Class2")

# class Class3(Class1):
#     def m(self):
#          print("In Class3")     
    
# class Class4(Class2, Class3):
#     def m(self):
#         print("In Class4")   

# obj = Class4()
# obj.m()


## MRO (method resolution order)
# class Class1:
#     def m(self):
#         print("In Class1")

# class Class2(Class1):
#     def m(self):
#         print("In Class2")
#         super().m()

# class Class3(Class1):
#     def m(self):
#         print("In Class3")
#         super().m()

# class Class4(Class2, Class3):
#     def m(self):
#         print("In Class4")   
#         super().m()
     
# print(Class4.mro())         # This will print list
# print(Class4.__mro__)       # This will print tuple


#############################################################################################
#############################################################################################


### Polymorphism

## Polymorphism in functions
## Here, duck typing enables functions to work with any objects regardless of their types.
# def add(a, b): # same fn can be used for doing all tasks
#     return a + b
# print(add(3, 4))           # Integer addition
# print(add("Hello, ", "World!"))  # String concatenation
# print(add([1, 2], [3, 4])) # List concatenation
## This is also an example of operator overloading where '+' is behaving respectively.

## Example of polymorphism in oops
# class Shape:
#     def area(self):
#         return "Undefined"

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

# shapes = [Rectangle(2, 3), Circle(5)]
# for shape in shapes:
#     print(f"Area: {shape.area()}")


## Compile-time Polymorphism --- Overloading
# def product(a, b):
#     p = a * b
#     print(p)

# def product(a, b, c):
#     p = a*b*c
#     print(p)

# product(4, 5) # Error - since latest version needs 3 parameters
# product(4, 5, 5) # 100

## Python does not support overloding, but there has methods to do so. 
# Use *args. Use default arguments. Use dispatch.
# def add(datatype, *args):
#     if datatype == 'int':
#         res = 0
#     elif datatype == 'str':
#         res = ''
#     for item in args:
#         res += item
#     print(res)
# add('int', 5, 6)
# add('str', 'Hi ', 'Geeks')

## Run-time Polymorphism --- Overriding
# class Animal:
#     def sound(self):
#         return "Some generic sound"

# class Dog(Animal):
#     def sound(self):
#         return "Bark"

# class Cat(Animal):
#     def sound(self):
#         return "Meow"

# # Polymorphic behavior
# animals = [Dog(), Cat(), Animal()]
# for animal in animals:
#     print(animal.sound())  # Calls the overridden method based on the object type


### Abstraction

## Example
# # Import required modules
# from abc import ABC, abstractmethod

# # Create Abstract base class
# class Car(ABC):
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
    
#     # Create abstract method      
#     @abstractmethod
#     def printDetails(self):   # abstract method
#         pass
  
#     # Create concrete method
#     def accelerate(self):     # concrete method
#         print("Speed up ...")
  
#     def break_applied(self):
#         print("Car stopped")

# # Create a child class
# class Hatchback(Car):
#     def printDetails(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Year:", self.year)
  
#     def sunroof(self):
#         print("Not having this feature")

# # Create a child class
# class Suv(Car):
#     def printDetails(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Year:", self.year)
  
#     def sunroof(self):
#         print("Available")

# # Create an instance of the Hatchback class
# car1 = Hatchback("Maruti", "Alto", "2022")

# # Call methods
# car1.printDetails()
# car1.accelerate()
# car1.sunroof()


## Abstract Classes
# from abc import ABC, abstractmethod
# # Define an abstract class
# class Animal(ABC):   
#     @abstractmethod
#     def sound(self):
#         pass  # This is an abstract method, no implementation here.

# # Concrete subclass of Animal
# class Dog(Animal):
#     def sound(self):
#         return "Bark"  # Providing the implementation of the abstract method

# # Create an instance of Dog
# dog = Dog()
# print(dog.sound())  # Output: Bark

## TypeError is caused when we call a abstract class directly.
# from abc import ABC, abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass
# # Trying to instantiate the abstract class directly
# # This will raise an error:
# # animal = Animal()  # TypeError: Can't instantiate abstract class Animal with abstract methods make_sound