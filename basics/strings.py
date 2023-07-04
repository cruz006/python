#   a string is a data structure where you store a collection of alphabets, words, or characters
#   to make a string a string, you need to wrap it in quotes as such:
message = "this is a string"
print(message + "\n")

#   for qoutes this is how you wouls do it
single = 'Single quote allow you to embed "double" quotes in your string.'
double = "Double quote allow you to embed 'single' quotes in your string."
triple = """Triple quotes allows to embed "double quotes" as well as 'single quotes' in your string. And can also span across multiple lines."""
print(single + " " + double + " " + triple + "\n")

#   this is how you can find the length of a certain string, i will be a new string
var1 = "this message is 33 characters long"
varLen = len(var1)
print(var1 + "\n")

#    then this is how you can use the index of a string to find a certain letter
#    using the index, it reads left to right starting at 0, and it goes by letter
snack = "Chocolate cookie."
print(snack[0] + "\n")

#    then this would be to find a whole word from it using the index
print(snack[10:16] + "\n")

#    these are ways that you could use index to print out the whole message
#   Stop value not provided, goes on forever
print(snack[0:] + "\n") 

#   Start value not provided (Stop value excluded according to syntax)
print(snack[:-1] + "\n")

#   This is also allowed
print(snack[:] + "\n")

#   then this is how you could print a list in reverse
num_string = "12345678910"
print(num_string[::-1] + "\n") 

#   this is how you could make it print every other one, the first digit 
#   will be the starting, then it is the order, and then the second order
print(num_string[0:-1:2] + "\n")

#   if you want to repeat a string, you would just multiply it
var2 = "hello"
print((var2 + " " )*3 + "\n")

#   this is how you can make a string upper case
var3 = str.capitalize('cookie')
print(var3 + "\n")

#   then this is how you can check if a string is in lower or upper case
snack = "cookie"
food = "Chips"
var4 = snack.isupper()
var5 = food.islower()
print(var4)
#   using the str() command, you can make the boolean into a string to be able to 
#   use a boolean and string in print()
print(str(var5) + "\n")

#   then this is how you can find a certain word within a string
str2 = "I got you a cookie"
str3 = "cookie"
print(str2.find(str3))

str1 = "I got you a cookie, do you like cookies?"
str2 = "cookie"
print(str1.count(str2))
