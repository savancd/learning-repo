"""
This one assignment to create our own Karel, did not achieve the result that I intended, but I did practiced and achieved interesting things and learned more.

"""


from karel.stanfordkarel import *

def main():
   
    while front_is_clear():
        corners()
        while beepers_present():
            move()
            if front_is_blocked():
                one_step_back()
                move()
                corners()
                while beepers_present():
                    move()
                    if front_is_blocked():
                        one_step_back_reversed()

def one_step_back_reversed():
    turn_back()
    move()
    turn_right()

def turn_back():
    for i in range(2):
        turn_left()

def one_step_back():
    for i in range(2):
        turn_left()
    move()
    turn_right()

def turn_right():
    for i in range(3):
        turn_left()

def corners():
    if no_beepers_present():
        put_beeper()
    while front_is_clear():
        move()
    turn_left()
        

# don't change this code
if __name__ == '__main__':
    main()