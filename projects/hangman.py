#   this is where we get the name of the user
name = input("What is your name? ")

#   now you greet them
print ("Hello, " + name, "Time to play hangman!")

#   wait time
import time
time.sleep(3)
print("Start guessing!")

#   this is where you will have the secret word and whatever you guess
#   you may use whatever word you want, i am using "secret"
word = "secret"
guess = ""

#   this determines the number of turns available, you may change this
#   to whatever you want
turns = 10
while turns>0:
    failed = 0

    #   for every character in word
    for char in word:
        if char in guess:
            print(char, end="")