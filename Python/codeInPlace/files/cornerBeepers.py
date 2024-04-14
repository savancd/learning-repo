# Places one beeper in each corner
from karel.stanfordkarel import *

def main():
    # repeat the body certain num of times
    for i in range(4):
        put_beeper()
        move()
        move()
        move()
        turn_left()