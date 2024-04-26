# Places certain number of objects using for loop
from karel.stanfordkarel import *

# define main
def main():
    move()
    # repeat put_beaper many times
    for i in range(12):
        put_beeper()
    move()
