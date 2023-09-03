#!/bin/python3
	
def main():
	book = "Dracula"
	author = "Bram Stoker"
	release_year = 1897
	goodreads_rating = 4.01
		
#	print(book)
#	print(author)
#	print(release_year)
#	print(goodreads_rating)
	

#    --	variable names in a single line using commas as separators --	
	
# def main():
#    book, author, release_year, goodreads_rating = 'Dracula', 'Bram Stoker', 1897, 4.01

 
#	-- With the print() method, I can use + sign to add variables with strings inside a print method --

#	print(book + " is a novel, from the " + author + ", published in " + str(release_year) + ". It has a rating of " + str(goodreads_rating) + " on goodreads. ")

	
	print(f"{book} is a novel written by {author}, published in {release_year}."
		f" It has rating of {goodreads_rating} on goodreads." )
		
if __name__ == "__main__":
	main()
