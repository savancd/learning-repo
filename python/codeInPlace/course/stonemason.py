from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    for i in range(3):
        column()
        back_to_position()
        next_column()
    column()
    back_to_position()


# next column position
def next_column():
    for i in range(4):
        move()

# back to original position
def back_to_position():
    turn_back()
    while front_is_clear():
        move()
    turn_left()

# make a column
def column():
    # going up and making the beeper column
        turn_left()
        for i in range(4):
            put_beeper()
            move()
        put_beeper()
    # going back to bottom position


def turn_back():
    for i in range(2):
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()
    

if __name__ == '__main__':
    main()