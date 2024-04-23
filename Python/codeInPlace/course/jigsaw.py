from karel.stanfordkarel import *

"""
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""


def main():
    
    move_and_pick_up()
    piece_in_place()
    initial_position()

# Defining move_and_pick_up that will go from starting position to beeper
# where it will pick it up before continuing further with placenment to 
# the position
def move_and_pick_up():
    # If there is no beepers it will move and when it reach the beeper 
    # it will pick it up and move one position further
    while no_beepers_present():
        move()
    pick_beeper()

# From the position of picking up the beeper to final position where
# it needs to drop the beeper
def piece_in_place():
    move()
    turn_left()
    for i in range(2):
        move()
    put_beeper()

def initial_position():
    # facing up
    reverse()
    # facing down
    while front_is_clear():
        move()
    turn_right()
    # facing initial position
    while front_is_clear():
        move()
    reverse()

    
# Defining to flip to another direction
def reverse():
    for i in range(2):
        turn_left()
    
# defining the turn_right
def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()