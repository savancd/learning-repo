# Places five beepers is each corner (Nested loops)
from karel.stanfordkarel import *
def main():
    # repeat once for each corner
    for i in range(4):
        put_five_beepers()
        move_to_next_corner()

# reposition karel to the next corner
def move_to_next_corner() :
    move()
    move()
    move()
    turn_left()

# places 5 beepers using a for loop
def put_five_beepers() :
    for i in range(5):
        put_beeper()