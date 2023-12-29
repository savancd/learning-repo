#	NOTES
#	Use pseudocode - marking with comments what should make and do



#	Hard coded the name

# input("What is your name? ")
# print("Hello Sava")


#	Variable

#	Ask user what is their name
name = input("What's your name? ")

#	Remove whitespace from str
name = name.strip()

#	Capitalize user's name
name = name.capitalize()

#	Title base capitalization
name = name.title()


#	Combine with "." ".title" ".name"
name = name.strip().title()

#	Split user's name into first name and last name
first, last = name.split(" ")

#	Say hello to user
print("Hello, ", end="")	# Name will print what is inputed as text
print(name)			# end will force name to the same line 




print(f"Hello, {name}")


# print(*object, sep=' ', end='\n', )

