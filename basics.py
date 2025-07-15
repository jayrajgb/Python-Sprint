### datatypes for numberic types:
### int, float, complex

# x = 1e3 # scientific float number

# x = 1E3 # scientific float number

# x = -1.7e10 # scientific float number

# x = 1j # complex number

# x = random.randrange(1,10) # get random number


#################################################################################
#################################################################################


### datatypes for text/letter types:
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
## Arithematic --> +  -  *  /  %  **  //
## Comparison --> ==  !=  >  <  >=  <= 
## Bitwise --> &  |  ~  ^  <<  >>
## Assignment --> +=  -=  *=  /=  %=  //=  **=  &=  |=  ^=  >>=  <<=  :=
## Logical --> and  or  not
## Identity --> is  is not
## Membership --> in  not in

