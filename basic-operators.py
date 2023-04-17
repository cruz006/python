#   this will be for anything math related and basic operators
#   this is an example of how you can use different kinds of math
number = 1 + 2 * 3 / 4.0
print(number)

#   this is how you can find an average
average = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10)/10
print(average)

#   here is an example of division, but this is called MOD
#   When it is 11/3, it can be divded 3 times which equals 9, and then the remainder is stored, which is 2
remainder = 11 % 3
print(remainder)

#    this is how you can use multiplication 
multiply = 7 * 2
print(multiply)

#   this is how you can use numbers to a power
cubed = 7 ** 2
print(cubed)

#   this is how you can use repeating words 
lotsofhellos = "hello " * 10
print(lotsofhellos)

#    then this is how you can use lists and operators to combine them into one
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

#   here is a way that you can use the operators to check how many items are in one list
x = object()
y = object()

# t
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

