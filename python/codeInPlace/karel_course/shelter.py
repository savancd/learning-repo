from karel.stanfordkarel import *

# File: shelter.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel 
# move to the beeper, pick it up, and
# return home.
def main():
    turn_right()
    move()
    turn_left()
    move()
    move()
    move()
    pick_and_turn()
    return_to_start()
    move()
    turn_right()


def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def pick_and_turn():
    pick_beeper()
    turn_left()
    turn_left()

def return_to_start():
    move()
    move()
    move()
    turn_right()

    
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()