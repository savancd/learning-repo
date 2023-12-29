#	Reference used for learning: https://pythonprogramminglanguage.com/randon-numbers/


import random

serbian_alphabet_mapping = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'Đ': 5, 'E': 6, 'F': 7, 'G': 8, 'H': 9, 'I': 10,
    'J': 11, 'K': 12, 'L': 13, 'Lj': 14, 'M': 15, 'N': 16, 'Nj': 17, 'O': 18, 'P': 19,
    'R': 20, 'S': 21, 'T': 22, 'Ć': 23, 'U': 24, 'V': 25, 'Z': 26, 'Š': 27, 'Đž': 28, 'Č': 29, 'Ž': 30
}

def calculate_numbers_from_name(name):
    name = name.upper()  # Convert the name to uppercase for consistent mapping
    numbers = {}
    result = []

    for letter in name:
        if letter in serbian_alphabet_mapping:
            if letter in numbers:
                result.append(numbers[letter])
            else:
                if len(numbers) < 10:
                    numbers[letter] = 30 + len(numbers) + 1
                else:
                    numbers[letter] = len(numbers) - 9
                result.append(serbian_alphabet_mapping[letter])
        else:
            result.append(0)  # Use 0 for characters not in the mapping

    return result

def generate_random_numbers(numbers, count=7):
    if len(numbers) >= count:
        random_numbers = random.sample(numbers, count)
    else:
        # If there are fewer numbers than required, generate the remaining numbers randomly
        random_numbers = random.sample(range(1, 40), count - len(numbers))
        random_numbers.extend(numbers)

    return random_numbers

def main():
    name = input("Enter a name: ")
    numbers = calculate_numbers_from_name(name)
    random_numbers = generate_random_numbers(numbers, count=7)

    print("Mapped numbers for the name:", numbers)
    print("Random 7 numbers:", random_numbers)

if __name__ == "__main__":
    main()
