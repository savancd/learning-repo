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

def main():
    name = input("Enter a name: ")
    numbers = calculate_numbers_from_name(name)

    print("Mapped numbers for the name:", numbers)

if __name__ == "__main__":
    main()
