# Importing random library

import random

# Number of sides on each die to roll (constant "NUM_SIDES")
# Using constants is good for updating with new vales
NUM_SIDES = 6

def main():
    # setting seed is usefull for debugging
    random.seed(1)
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    
    print("Dice have" , NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)

if __name__ == '__main__':
    main()