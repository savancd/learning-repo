"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    while front_is_clear():
        move_and_pick()
    back_one_step()
    #   go back two steps because there is more to pick up and it's located in the midle of table
    for i in range(2):
        move()
    # continues picking and following the path while searching for beepers
    while front_is_clear():
        move_and_pick()

# checking is there an beepers and if there is, it's continuing path
def move_and_pick():    
    while beepers_present():
        pick_beeper()
        move()  
    back_one_step()  
    check_the_beeper()
    find_beepers()

#   Going to previous position when it reaches end of beepers(no beepers)
def back_one_step():
    for i in range(2):
        turn_left()
   

def check_the_beeper():
    if beepers_present():
        pick_beeper()
    move()
    back_one_step()

def find_beepers():
    if beepers_present():
        move()
    else:
        turn_left()
    move()

def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()