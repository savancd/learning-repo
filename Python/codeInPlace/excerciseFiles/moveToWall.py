# Uses a "while" loop to move Karel until it hits 
# a wall. Works on any sized world
from karel.stanfordkarel import *

# the program starts with main
def main():
    # call the "move_to_wall" function
    move_to_wall()

# this is a very usefull function
def move_to_wall():
    # repeat the body while condition holds
    while front_is_clear():
        move()