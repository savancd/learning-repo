"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *


def main():
    while beepers_present():
            follow_straight_trail()
            step_backwards()
            # Check left
            turn_left()
            move()
            if no_beepers_present():
                # Trail doesn't continue to the left;
                # Go right
                step_backwards()
                turn_around()
                move()
                # Here the next iteration of the loop will check if there is a beeper; if there is we will keep going and if not we will stop!
        
def follow_straight_trail():
    while beepers_present():
        pick_beeper()
        move()

def step_backwards():
    """
    Turn around and go back one step, 
    then face the same way you were when you started
    """
    turn_around()
    move()
    turn_around()

def turn_around():
    turn_left()
    turn_left()

"""
    pick_beeper()
    clean_row()
    back_to_pos()
    pick_beeper()
    clean_row()
    back_to_pos()
    turn_right()
    pick_beeper()
    clean_row()
    one_step_back()
    turn_left()
    clean_row()
    one_step_back()
    turn_left()
    clean_row()
    one_step_back()
    turn_right()
    clean_row()
    one_step_back()
    turn_right()
    clean_row()


def clean_row():
    move()
    while beepers_present():
        pick_beeper()
        move()

def one_step_back():
    reverse()
    move()

def back_to_pos():
    reverse()
    move()
    turn_right()
    move()


def reverse():
    for i in range(2):
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()
"""


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()