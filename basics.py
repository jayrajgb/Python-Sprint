### Case Sensitivity
# a case-sensitive language is one where uppercase 
# and lowercase letters are treated as distinct characters.
# Case-sensitive --- py, cpp, c, java, js (age, Age, AGE are different variables)
# Case-insensitive --- html, sql, php


### Datatypes for numeric types:
### int, float, complex

# x = 1e3 # scientific float number

# x = 1E3 # scientific float number

# x = -1.7e10 # scientific float number

# x = 1j # complex number

# x = random.randrange(1,10) # get random number


#################################################################################
#################################################################################


### Datatypes for text/letter types:
### str (only)

# x = 'b' # string of length 1

# length = len("hello, YOU") # returns length

# check if exists in a string --- in
# txt = "hello world"
# print("world" in txt) # returns true

# check if does not exists in a string --- not in
# txt = "hello world"
# print("world" not in txt) # returns false

# can use it with if statements as well
# if "world" in txt:
#   printf("exists")
# if "world" not in txt:
#   printf("does not exists")

# string slicing
# x = "abcde"
# print(x[1:4]) # takes positions 1,2,3 & 4 not included
# print(x[-4:-1]) # takes positions 1,2,3 & 4 not included
# make sure always its [start:end]

# methods for strings
# capitalize() - Capital          strip() - no whitespace
# upper() - uppercase             replace("W","M") - replace an element/part
# lower() - lowercase             startswith(), endswith(), join(), etc.
# split(",") - splits in two parts (from left) returning a list 
# rsplit(",") - splits in two parts (from right) returning a list 

# print("abcdea".find('a'))   # returns 0
# print("abcdea".rfind('a'))  # returns 5
# print("abcdea".index('ea', 2, 6))  # returns 4
# If not found, the find() returns -1, but index() raises exception

# x = "hello" + " " + "you"     # valid
# x = "hello" + 36              # not valid

# use format() method or f-string

# x = "hello {num}".format(num=36)
# x = "hello {}".format(36)
# print(x)

# num = 36
# x = f"hello {num}"
# print(x)

# num = 36.2222
# x = f"hello {num: .2f}"
# print(x)

# num = 5
# x = f"binary of {num} is {num: b}"
# print(x)
# x = f"octal of {num} is {num: o}"
# print(x)
# x = f"decimal of {num} is {num: d}"
# print(x)
# x = f"float of {num} is {num: f}"
# print(x)
# x = f"hexadecimal of {num} is {num: x}"
# print(x)

# escape sequence characters
# \' - single quote           \b - backspace
# \\ - backslash              \r - carraige return, returns right side text
# \n - new line               \ooo - octal value
# \t - tab                    \xhh - hex value

### boolean
# bool(), <, >, <=, >=, !=, == returns True or False
# bool(False)
# bool(None)
# bool(0)
# bool("")      # returns false
# bool(())
# bool([])
# bool({})


#################################################################################
#################################################################################


### Operators

# Arithematic --> +  -  *  /  %  **  //

# Comparison --> ==  !=  >  <  >=  <= 

# Bitwise --> &  |  ~  ^  <<  >>

# Assignment --> +=  -=  *=  /=  %=  //=  **=  &=  |=  ^=  >>=  <<=  :=

# Logical --> and  or  not

# Identity --> is  is not

# Membership --> in  not in


#################################################################################
#################################################################################


### Conditional Statements

## if, elif, else
# a = 4
# b = 5
# if a > b:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")

# a = 4
# b = 5
# c = 6
# if a > b and c > a:
#   print("Both conditions are True")

# a = 4
# b = 5
# c = 6
# if a > b or c > a:
#   print("Both conditions are True")

# a = 4
# b = 5
# c = 6
# if not a > b:
#   print("Both conditions are True")

## pass is used to avoid error
# a = 33
# b = 200
# if b > a:
#   pass

## there is no switch, python uses match
# num = 2
# match num:
#     case 1:
#         print("One")
#     case 2 | 3:
#         print("Two or Three")
#     case _: # wildcard/default statement
#         print("Other number")


#################################################################################
#################################################################################


### Loops

## while loop
# i = 1
# while i < 5:
#   print(i)
#   i += 1

## for loop
# for x in range(6): # start is default 0.
#   print(x)
# for x in range(2, 30, 3): # start with 2, end on 30, increment with 3
#   print(x)

## for-else --- executes after for loop executes
## The else block will NOT be executed if the loop is stopped by a break statement.
# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!") 

## for loop with no content, put in the pass statement to avoid getting an error.
# for x in [0, 1, 2]:
#   pass

## With the break statement we can stop the loop even if the while condition is true

## With the continue statement we can stop the current iteration, and continue with the next


#################################################################################
#################################################################################


### Functions --- a block that only executes when called

# def my_function():
#   print("Hello from a function")
# my_function()

## The terms parameter and argument can be used for the same thing: information that are passed into a function.

## A parameter is the variable listed inside the parentheses in the function definition.

## An argument is the value that is sent to the function when it is called.

## No. of arguments passed, should match no. of parameters, else error.

## If no. of arguments is not known, use *args in parameters
# def my_function(*kids):
#   print("The youngest child is " + kids[2])
#   print(type(kids)) # tuple
# my_function("Emil", "Tobias", "Linus")

## arbitrary arguments --- *args is a tuple

## Keyword arguments
# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)
# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# def my_function(**kid):
#   print("His last name is " + kid["lname"])
#   print(type(kid)) # dict
# my_function(fname = "Tobias", lname = "Refsnes")

## keyword arbitrary arguments --- **kwargs is a tuple

## Default parameter
# def my_function(country = "Norway"):
#   print("I am from " + country)
# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

## Compare positional and keyword arguments?


## Lambda Function

# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

# x = lambda a : a + 10
# print(x(5))

# x = lambda a, b : a * b
# print(x(5, 6))

# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))

## The power of lambda is better shown when you use them as an anonymous function inside another function.
# def myfunc(n):
#   return lambda a : a * n
# mydoubler = myfunc(2)
# print(mydoubler(11))

# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)
# mytripler = myfunc(3)

# print(mydoubler(11))
# print(mytripler(11))
