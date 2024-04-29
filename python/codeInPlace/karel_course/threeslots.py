"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    """
    Place beepers in the bottom row of a world with 3 slots.
    """
    while front_is_clear():
        fill_spot_and_back_to_pos()
        move()
    fill_spot_and_back_to_pos()
    

def fill_spot_and_back_to_pos():
    turn_right()
    move()
    put_beeper()
    reverse()
    move()
    turn_right()

def reverse():
    for i in range(2):
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()