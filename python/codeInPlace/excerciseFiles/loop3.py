# This tells python who Karel is!
from karel.stanfordkarel import *

# this program executes in a special function called main
def main():
    for i in range(4):
        move()
        place_beeper()

def place_beeper():
    for i in range(4):
        put_beeper()
    turn_left()

# This is "boilerplate" code which launches your code
# when you hit the run button
if __name__ == '__main__':
    main()
