from karel.stanfordkarel import *

"""
This was optional challenge for the course that I did (Unsucessfully) I did no manage to make it work properly.
I manage to solve the middle point in the 5x5 world but 6x5 world always was on wrong position placenment of Karel.
When I manage to make it work on 6x5 world then is the issue with 5x5 world, so it doesn't work on every world 
properly in the same time.


Edit:

At the few days later attempt I managed tp fond a solution to the problem of middle karel
"""

from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should be able to find
the midpoint
"""

def main():
   
    row_of_beepers()
    ends()
    last_beep()

def last_beep():
    turn_back()
    move()
    put_beeper()
    if not_facing_east():
        turn_back()



    # remove end beepers
def ends():
    pick_beeper()
    turn_back()
    while front_is_clear():
        move()
    pick_beeper()
    if not_facing_east():
        turn_back()
    step_back()

def step_back():
    if no_beepers_present():
        move()
    while beepers_present():
        beep_present()


def beep_present():
    while beepers_present():
            move()
    turn_back()
    move()
    pick_beeper()
    move()

def next_end():
    while beepers_present():
        move()
    step_back()


  # put karel in one row
def row_of_beepers():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

def turn_back():
    for i in range(2):
        turn_left()

if __name__ == '__main__':
    main()