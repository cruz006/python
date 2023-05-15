#   importing the time module
import time

#   greeting
name = input("What is your name? \n")
print ("Hello, " + name, "it's time to play hangman!")

#   wait for 2 second
time.sleep(2)

print("Hint: It's Mrs. Smith's favorite rhetorical device!")
print ("Start guessing...")
time.sleep(1)

#   this will be the word you need to find
word = ("zeugma")

#   makes the things you guess
guesses = ''

#   number of terms you have
turns = 6

#   Create a while loop for the game
while turns > 0:         

    #   counter
    failed = 0             

    #   goes through word to check 
    for char in word:      

    #   checks if any words you guess are correct
        if char in guesses:    
    
        #   prints what you guess
            print (char,end=""),    

        else:
        #   appears if you are wrong
            print (" _ ",end=""),     
       
        #   increases fails
            failed += 1    


    #   if fail is equal to 0
    if failed == 0:        
        print (" You won")
   
        break  

    #   ask again
    guess = input(", guess a letter: ") 

    #   sets your guess to the guesses taken and function for if not
    guesses += guess                    
    if guess not in word:  
 
     #  removes a turn if wrong
        turns -= 1        
        print ("Wrong")  
 
    #   tells you how many turns you have left
        print ("You have", + turns, 'more guesses' )
 
    #   condional for if you lose
        if turns == 0:           
            print ("You Lose, the word was " + word )
    