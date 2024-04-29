from karel.stanfordkarel import *

# File: piles.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel
# pick up all the beepers in the world.
def main():
    move()
    for i in range(2):
        pick()
    last_pick()

def last_pick():
    for i in range(10):
        pick_beeper()
    move()

def pick():
    for i in range(10):
        pick_beeper()
    move()
    move()
   
   
   
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()