#   this file will contain most of the commands that are needed when learning python

#   this for loop prints all numbers between 1 and 10. 
for i in range(1,10):
    print(i)

#   this is a type command, which is used to check the type of an object in your code. 
#   when you print it, it will show you which class the object is
my_str = "Why hello there"
print(type(my_str))

my_int = 5
print(type(my_int))

cnum = 3 + 2j
print(type(cnum))

rnum = 3.14
print(type(rnum))

#   this is the input command, where it takes your input
#   then, it prints your input
var1 = input("Hello, your name is: ")
print("Hello there " + var1)

var2 = input("Pick any number: ")
print("The number you said is " + var2 + ", correct?")

#   the len command checks the length of anything
#   the str command here is used to make the length(an interger),
#   into a string to be able to print it
var3 = input("Type anything you want here: ")
print("What you typed is " + str(len(var3)) + " characters long.")

#   the str string can be used for many uses
var4 = 1000
print(str(var4))