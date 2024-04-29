from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    
    while front_is_clear():
        one_row_beepers()
        row_back()
        row_up()

# one row up facing right side
def row_up():
    # Because at this point is facing left, if right side of karel is clear 
    # without wall, it's gonna continue into next row and continue as long
    # there is clear path
    if right_is_clear():
        turn_right()
        move()
        turn_right()
    # If the right side of karel that is facing left, blocked. That means that 
    # it reached the top of box and it needs to go back to last position
    if right_is_blocked():
        turn_back()
        while front_is_clear():
            move()
        


# back to position, one level up
def row_back():
    while front_is_blocked():
        turn_back()
    move()
    while front_is_clear():
        move()
    

    

# making one row
def one_row_beepers():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()  

def turn_back():
    for i in range(2):
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()