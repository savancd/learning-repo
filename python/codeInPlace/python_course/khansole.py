import random

def main():
    print("Khansole Academy")

    # numbers 
    num1 = 51
    num2 = 79

    ans = num1 + num2

    # Printing the question for the user
    # each num must be converted to string = str(num1) 
    print("What is: " + str(num1) + " " + "+"  + " " + str(num2) + "?")
    
    # user input
    user_input = int(input("Your answer: "))

    #print(user_input)

    if user_input == ans:
        print("Correct! ") 
    else:
        print("Incorrect.")
        print("The expected answer is " + str(ans))



if __name__ == '__main__':
    main()