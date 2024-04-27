"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
   top_on_the_stem()
   flower_beepers()
   next_flower_beepers()
   back_to_bottom_position()



# defining going to the bottom and getting into right direction and position
def back_to_bottom_position():
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    while front_is_clear():
        move()

# going to the top of the nect step where is making new flower
def next_flower_beepers():
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    top_on_the_stem()
    flower_beepers()

# making the flower of the beepers
def flower_beepers():
    while no_beepers_present():
        put_beeper()
        move()
        turn_left()
    move()

def top_on_the_stem():
   # moving to the end while is clear in front
    while front_is_clear():
        move()
    turn_left()

    while right_is_blocked():
        move()
    # facing the right
    turn_right()
#
# end of the stem
#

def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()