"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    while front_is_clear():
        step_up_and_place()
        step_down_and_place()

# defining the step up function, it goes from starting position to one 
# position up
def step_up_and_place():
    put_beeper()
    turn_left()
    move()
    turn_right()
    if front_is_clear():
        move()

# defining the step down function
def step_down_and_place():
    put_beeper()
    # facing right
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    if front_is_clear():
        move()

# defining the turn right function
def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()