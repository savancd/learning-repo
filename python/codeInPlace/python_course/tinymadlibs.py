
SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my " # adjective noun verb


def main():
    adjective = input("Please type an adjective and press enter. ")
    noun = input("Please type a noun and press enter. ")
    verb = input("Please type a verb and press enter. ")

    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()