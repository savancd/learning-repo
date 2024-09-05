#	Escaping \"friend=" should show the sign behind 
#	escape and would print "friend"


name = input("What is your name:").strip().title() 
# best way of writing lines of code in one line of code
# good way to write code in separate lines of code to be easier readable


# Remove whitespace from str
#name = name.strip()

# Capitalise user's name
#name = name.capitalize()

# Remove whitespce from str and capitalize user's name and "title" last name
#name = name.strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")


# Hello to user {name} is new way of writing it- old versio was ("Hello, " + name)
print(f"Hello, {first}")
	



