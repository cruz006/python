#   a string is a data structure where you store a collection of alphabets, words, or characters
#   to make a string a string, you need to wrap it in quotes as such:
message = "this is a string"
print(message)

#   for qoutes this is how you wouls do it
single = 'Single quote allow you to embed "double" quotes in your string.'
double = "Double quote allow you to embed 'single' quotes in your string."
triple = """Triple quotes allows to embed "double quotes" as well as 'single quotes' in your string. And can also span across multiple lines."""
print(single + " " + double + " " + triple)

#   this is how you can find the length of a certain string, i will be using the previous strings
var1 = len(single)
print(var1)

#    then this is how you can use the index of a string to find a certain letter
#    using the index, it reads left to right starting at 0, and it goes by letter
snack = "Chocolate cookie."
print(snack[0])

#    then this would be to find a whole word from it using the index
print(snack[10:16])

#    these are ways that you could use index to print out the whole message
#   Stop value not provided, goes on forever
print(snack[0:]) 

#   Start value not provided (Stop value excluded according to syntax)
print(snack[:-1])

#   This is also allowed
print(snack[:])

#   then this is how you could print a list in reverse
num_string = "12345678910"
print(num_string[::-1]) 

#   this is how you could make it print every other one, the first digit 
#   will be the starting, then it is the order, and then the second order
print(num_string[0:-1:2])

#   if you want to repeat a string, you would just multiply it
var2 = "hello"
print((var2 + " " )*3)

