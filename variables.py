#this is a tutorial for Python, IN Python
#you can assign variables values as well as quotes or really anything you want, all you need to do is print it
var=3
print("1+2=", var)
var1="do you see what i mean?"
print(var1)
#press enter to see the results

#Assignments can be done on more than one variable "simultaneously" on the same line like this
a, b = 3, 4
print(a,b)

# This will not work! this is since 
# one = 1
# two = 2
# hello = "hello"

# print(one + two + hello)

# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code, this is just to be able to see the difference between each my, and then prints them
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

#message, or msg also works
msg="Hello World!"
print(msg)

#myint is my interger
# mystring is my string myfloat is a whole number with a deicaml point to be exact
# str is equal to	Text
# int, float, complex are all Numeric
# list, tuple, range count as Sequences
# dict is for Mapping
# set, frozenset are for Sets
# bool is Boolean
# bytes, bytearray, memoryview are all Binary