#	Step 1:	Importing the necessary modules		
#	Importing the tkinter for creating graphical user interface and importing the random

import tkinter as tk
import random

#	Step 2: Alphabet Mapping

alphabet_mapping = {
	'A': 1, 'B': 2, 'C': 3, 'D': 4, 'Đ': 5, 'E': 6, 'F': 7, 'G': 8, 'H': 9, 'I': 10,
	'J': 11, 'K': 12, 'L': 13, 'Lj': 14, 'M': 15, 'N': 16, 'Nj': 17, 'O': 18, 'P': 19,
	'R': 20, 'S': 21, 'T': 22, 'Ć': 23, 'U': 24, 'V': 25, 'Z': 26, 'Š': 27, 'Đž': 28, 'Č': 29, 'Ž': 30
}

#	Define a dictionary that maps alphabet characters to corestponding numbers.
#	Mapping is used to convert a name to numbers

#	Step 3: Define Function to calculate numver from text

def calculate_num_from_text(text):
	text = text.upper()	#	Converting the text to uppercase
	numbers = {}
	result = []
	
#	Create a function that takes a text as input and converts it to a list of numbers based on the alphabet mapping

for letter in text:
	if letter in alphabet_mapping:
		if letter in numbers:
			result.append(numbers[letter])
		else:
			if len(numbers) < 10:
				numbers[letter]= 30 + len[numbers] + 1
			else:
				numbers[letter] = len(numbers) - 9
			result.append(0)	#	Use 0 for characters not in the mapping
return result
			
#	Code converts each character of the input text to its corresponding num and construct the list and if the character is not on the 	#	mapping. It is represented as 0


    
#	Step 4:	Define function to generate random num
def generate_ramdom_numbers(numbers, count=7):
#	Generate random numbers from the inpput list
	random_numbers = random.sample(numbers, count)
	
#	Ensure at least numbers are present
while len(random_numbers)<coount:
	random_numbers += random.sample(numbers, count - len(random_numbers))
		
return random_numbers
	
#	This function generate random num based on a list of numbers and return a list of random numbers

#	Step 5:	Define function to generate numbers and show popup
def generate_num_pop():
	user_input = input_get()	#	Get user's input text
	numbers = calculate_num_from_text(user_input)
	random_numbers = generate_random_numbers(numbers)
	
#	Create congratulation popup window
	congratulation_popup = tk.Toplevel(main_window)
	congratulatio_popup.title("Congratulation!")
	
#	Display a message with the random num in the popup
	message = f"Random Numbers: {random_numbers}"
	message_label.pack(padx=10, pady=10)

#	This function gets the iser's input from the field, calculates numbers, generate random numbers and displays a popup

#	Step 6:	Main window
	main_window = tk.Tk()
	main_window.title("Aplhabet to numbers")
	
#	This code create the main window

#	Step 7:	Add input field and generate button
	input_label = tk.Label(main_window, text="Enter the text:")
	input_entry.pack(padx=10, pady=10)
	
	generate_button = tk.Button(main_window, text="Generate Numbers", command=generate_num_pop)
	generate_button.pack(padx=10, pady=10)
	
#	Add an input field for the user to enter their text and a button

#	Step 8:	Start the GUI
	main_window.mainloop()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	




































