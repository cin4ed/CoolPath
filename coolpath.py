import os

# Clarifying things:
# PATH = The environment variable
# path = A directory path


# Getting the PATH variable
def getPATH():
	STR_PATH = os.environ.get('PATH')
	return STR_PATH

# Function to display a cool view of the path
def displayPathListForm(STR_PATH):

	# Converting the PATH string into a list to modify it
	PATH = list(STR_PATH)

	# Counter for the numbered list, and insertion of the first path in the PATH with the number '1'
	counter = 1
	PATH.insert(0, str(counter) + ': ')

	# Cheking each letter in the PATH
	for letter in range(0, len(PATH)):

		# Looking for ':' to change it for '\n'
		if PATH[letter] == ':':
			counter = counter + 1 # Taiming the counter for the numbered list

			PATH[letter] = '\n' # Changing the ':' for '\n'

			PATH.insert(letter + 1, str(counter) + ': ') # Inserting the number order

	PATH = ''.join(PATH) # Reverting the list into a string

	print(PATH) # Printing the PATH with the changes made

# Main function of the program
def main():
	STR_PATH = getPATH()
	displayPathListForm(STR_PATH)

main()