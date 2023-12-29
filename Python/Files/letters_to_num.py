import random

serbian_alphabet_mapping = {
    'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Д': 5, 'Ђ': 6, 'Е': 7, 'Ж': 8, 'З': 9, 'И': 10,
    'Ј': 11, 'К': 12, 'Л': 13, 'Љ': 14, 'М': 15, 'Н': 16, 'Њ': 17, 'О': 18, 'П': 19,
    'Р': 20, 'С': 21, 'Т': 22, 'Ћ': 23, 'У': 24, 'Ф': 25, 'Х': 26, 'Ц': 27, 'Ч': 28,
    'Џ': 29, 'Ш': 30, ' ': 0
}

def calculate_numbers_from_name(name):
    name = name.upper()  # Convert the name to uppercase for consistent mapping
    numbers = []

    for letter in name:
        if letter in serbian_alphabet_mapping:
            numbers.append(serbian_alphabet_mapping[letter])
        else:
            numbers.append(0)  # Use 0 for characters not in the mapping

    return numbers

def calculate_average_numbers(numbers, birth_month, birth_date, birth_year):
    # Generate 7 average numbers from the sum of name numbers, birth month, birth date, and birth year
    total_sum = sum(numbers) + int(birth_month) + int(birth_date) + int(birth_year)
    average_numbers = [random.randint(1, 39) for _ in range(7)]
    return average_numbers

def main():
    name = input("Enter a name: ")

    birth_month = input("Enter the birth month (e.g., 5): ")
    birth_date = input("Enter the birth date (e.g., 15): ")
    birth_year = input("Enter the birth year (e.g., 1990): ")

    name_numbers = calculate_numbers_from_name(name)
    average_numbers = calculate_average_numbers(name_numbers, birth_month, birth_date, birth_year)

    print("Mapped numbers for the name:", name_numbers)
    print("Average numbers:", average_numbers)

if __name__ == "__main__":
    main()
