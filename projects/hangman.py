#   this will be the code needed for the hangman game code
#   this is where we get the name of the user
print('Hello, what is your name?')
my_name = input()

#   now you greet them
print('Hello, {}'.format (my_name) + ' would you like to play hangman? Please enter "yes" or "no" to continue')

game_on = "yes"
if input() == game_on:
    var1 = "very well"
    print(var1)


game_off = "no"
if input() == game_off:
    var2 = "dam, ok. you suck"
    print(var2)
