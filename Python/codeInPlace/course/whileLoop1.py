from karel.stanfordkarel import *

def main():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    turn_left()
    move()
    turn_left()
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    turn_left()
    move()
    turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()