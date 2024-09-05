from karel.stanfordkarel import *

def main():
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    turn_right()
    move()
    put_beeper()
    move()

# Karel turns to right
def turn_right():
    turn_left()
    turn_left()
    turn_left()


if __name__ == "__main__":
    main()