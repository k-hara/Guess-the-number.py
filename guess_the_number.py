# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math


# initialize global variables used in your code
num_range = 100
num_remaining = int(math.ceil(math.log(num_range, 2))) 
secret_num = random.randrange(0, num_range)

# helper function to start and restart the game
def new_game():
     global num_remaining 
     num_remaining = int(math.ceil(math.log(num_range, 2))) 
     print "New game. Range is from 0 to", num_range
     print "Number of remaining guesses is",num_remaining
     global secret_num
     secret_num = random.randrange(0, num_range)
     return
     
     

# define event handlers for control panel
def range100():
    global num_range
    num_range = 100
    new_game()
    return
   
    # button that changes range to range [0,100) and restarts
    
    # remove this when you add your code    

    

def range1000(): 
    global num_range
    num_range = 1000
    new_game()
    return
  
    
    
    # button that changes range to range [0,1000) and restarts
    
    # remove this when you add your code    
    pass
    
def input_guess(guess):
    num_guess = int(guess)
    global num_remaining
    num_remaining = num_remaining - 1
    print "Guess was", num_guess
    print "Number of remaining guesses is",num_remaining
    if num_guess == secret_num:
        print "Correct!"
        new_game()
    elif (num_remaining > 0) and (secret_num > num_guess):
        print "Higher"
    elif (num_remaining > 0) and (secret_num < num_guess):
        print "Lower"
    else:
        print " You lose!"
        new_game()
           
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)


# register event handlers for control elements
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)



# call new_game and start frame

new_game()

# always remember to check your completed program against the grading rubric
