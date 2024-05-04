"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

def main():
    # always must be converted first into float
    side_1 = float(input("What is the length of side 1? "))
    side_2 = float(input("What is the length of side 2? "))
    side_3 = float(input("What is the length of side 3? "))

    # Always must be converted back into str - make sure to cast it to a str when concatenating!
    print("The perimeter of the triangle is " + str(side_1 + side_2 + side_3))


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()4