# Useful constants to help make the math easier and cleaner!
DAYS_PER_YEAR = 365
HOURS_PER_DAY = 24
MIN_PER_HOUR = 60
SEC_PER_MIN = 60

def main():
    # We can get the number of seconds per year by multiplying the handy constants above!
    print("There are " + str(DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN) + " seconds in a year!")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()