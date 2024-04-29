from karel.stanfordkarel import *

def main():
    """
    Traverses 5 variable length corridors and place beepers at the ends of them if there aren't already beepers there.
    """
    for i in range(4):
        move_to_end()
        turn()
        next_corridor()
    move_to_end()
    turn()
    back_to_start()

def back_to_start():
    while front_is_clear():
        move()
    turn()
       
def next_corridor():
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_right()

def move_to_end():
    while front_is_clear():
        move()
    if no_beepers_present():
        put_beeper()

def turn():
    for i in range(2):
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
