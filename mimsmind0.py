""" 
usage: python mimsmind0.py [length]

In this version, the program generates a random number with number of digits equal to length. 
If the command line argument length is not provided, the default value is 1. 
Then, the program prompts the user to type in a guess, informing the user of the number of digits expected. 
The program will then read the user input, and provide basic feedback to the user. 
If the guess is correct, the program will print a congratulatory message with the number of guesses made and terminate the game. 
Otherwise, the program will print a message asking the user to guess a higher or lower number, 
and prompt the user to type in the next guess.

"""

# Imports
import random
import sys

# Body

# define global variables
numberDigits = 1 # number of digits
mainNumber = 0 # the corrent answer to the game
numberTries = 0

# function to check if the command line argument is valid or not, if valid assign the value to numberDigits
# def CheckCommandLineArgument(argv):
# 	if(len(argv) == 1):
# 		return True
# 	elif(len(argv) == 2):
# 		# check if the 2nd input is actually an integer
# 		try:
# 			userLengthInput = int(argv[1])
# 			if(userLengthInput <= 0):
# 				raise ValueError
# 			else:
# 				numberDigits = userLengthInput
# 			return True
# 		except ValueError:
# 			print("\n*********************************************")
# 			print("Invalid User Input: " + str(argv[1]) + ". Please Enter A Valid Positive Integer")
			# return False

# function to start the game
def StartGame(numberDigits):
	# generate a random number based on the length input by the user
	upperLimit = (10**numberDigits) - 1
	mainNumber = random.randint(0, upperLimit)
	# print(mainNumber)

	print("\nLet's Play The mimsmind0 Game.\n")

	StartGuessing(numberDigits, mainNumber, numberTries)

def StartGuessing(numberDigits, mainNumber, numberTries):
	userInput = 0
	# continuously ask for User Input and count the number of guesses it took to guess the right answer
	while True:
		try:
			userInput = int(input("Enter A " + str(numberDigits) + " Digit Number: "))
			if(len(str(userInput)) != numberDigits):
				raise ValueError
			numberTries += 1

			if(userInput == mainNumber):
				print("Congratulations. You Have Guessed The Corrent Number In " + str(numberTries) + " Tries.")
				break
			elif(userInput < mainNumber):
				print("Guess A Higher Number. Try Again!")
			elif(userInput > mainNumber):
				print("Guess A Lower Number. Try Again!")
		except ValueError:
			print("Invalid Input. Enter A Valid " + str(numberDigits) + " Integer.")
			continue

def main():

	numberDigits = 1 # number of digits
	mainNumber = 0 # the corrent answer to the game
	numberTries = 0
	
	# check user input
	if(len(sys.argv) == 1):
		StartGame(numberDigits)
	elif(len(sys.argv) == 2):
		# check if the 2nd input is actually an integer
		try:
			userLengthInput = int(sys.argv[1])
			if(userLengthInput <= 0):
				raise ValueError
			else:
				numberDigits = userLengthInput
				StartGame(numberDigits, numberTries)
			return True
		except ValueError:
			print("\n*********************************************")
			print("Invalid User Input: " + str(sys.argv[1]) + ". Please Enter A Valid Positive Integer")
			return False

if __name__ == '__main__':
	main()
