"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    """ Turns Karel until facing a wall. """
    
    while front_is_clear(): # If there is no wall in front it is gonna turn until it ends up facing the wall
        turn_left()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()