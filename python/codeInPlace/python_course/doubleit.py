
def main():
    #   user input a num
    curr_value = int(input("Enter a number: "))
    # while curr_value is less then 100 it should continue to print
    while curr_value < 100:
        # multiplying curr_value with it self by two
        curr_value = curr_value * 2
        print(curr_value)
        
    

if __name__ == '__main__':
    main()