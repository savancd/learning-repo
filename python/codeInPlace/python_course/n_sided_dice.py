import random

def main():
    side_number = int(input("How many sides does your dice have? "))
    roll = random.randint(1, side_number)

    print("Your roll is " , str(roll))

if __name__ == '__main__':
    main()