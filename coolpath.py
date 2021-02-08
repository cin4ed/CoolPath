import os

# Clarifying things:
# PATH = The environment variable
# path = A directory path

# Colors for console displaying
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Getting the PATH variable
def getPATH():
	PATH = os.environ.get('PATH')
	return PATH

# This function divide each path in the PATH variable and store it in another list. crazy no?
def listOfPaths(PATH):

	listOfPaths = list(PATH) # Convert the String PATH to a list PATH

	newList = [[]] # Inside this list will be the paths.


	# Sincerly I don't even know how I made the following, so I hope you understand me in my next comments sorry.

	# This for is to divide the paths inside the listOfPaths into another lists inside this
	counterA = 0
	for letter in listOfPaths:
		# Accordingly to the ":" found, will increase the counter by 1 making separate lists
		if letter != ':':
			newList[counterA].append(letter)
		else:
			newList.append([])
			counterA += 1

	# This for convert the lists inside listOfPaths into strings 
	counterB = 0
	for lista in newList: # Yes, lista means list in spanish, list is a reserved keyword so i don't want problems :P
		newList[counterB] = ''.join(lista)
		counterB += 1 

	return newList


# Function to display a cool view of the path
def listView(PATH):

	# For the moment this print the paths with a header number before each one :)
	counter = 1
	for path in PATH:
		print(bcolors.HEADER + str(counter) + ": " + bcolors.ENDC + path)
		counter += 1


# Main function of the program
def main():
	listView(PATH)


PATH = listOfPaths(getPATH())
main()