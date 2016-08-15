"""
Version 1: 'Bulls and Cows' Feedback

After you have gotten Version 0 working, you can proceed to implement this slightly more advanced version.

usage: python mimsmind1.py [length]
Once again, the program generates a random number with number of digits equal to length. 
If the command line argument length is not provided, the default value is 3. 
This means that, by default, the random number is in the range of 000 and 999. 

In this version, the program will establish a maximum number of rounds, maxrounds, equal to (2^length) + length. 
For example, if length = 3, then maxrounds = 11.

Then, the program prompts the user to type in a guess, informing the user of the number of digits expected. 
The program will then read the user input, and provide 'bulls and cows' feedback to the user. 
A matching digit in the correct position will result in a 'bull', 
while a matching digit in the wrong position will result in a 'cow'. 
For example, if the correct answer is '123', and the guess is '324', 
then the feedback will be one bull (for the digit '2') and one cow (for the digit '3'). 
More examples are provided below.

At each round, if the user guess is incorrect and maxrounds is not yet reached, 
the program should increment the counter for round and issue a new prompt for user input. 
Otherwise, the program should print a congratulatory or an apologetic message with the number of guesses made, 
and terminate the game.

"""

# Imports
import random
import sys

# Body

# define global variables
numberDigits = 3 # number of digits
mainNumber = 0 # the corrent answer to the game
numberTries = 0

# function to start the game
def StartGame(numberDigits):
	# generate a random number based on the length input by the user
	upperLimit = (10**numberDigits) - 1
	mainNumber = random.randint(0, upperLimit)
	mainNumber = str(mainNumber).zfill(numberDigits)
	numberTries = (2**numberDigits) + numberDigits

	print(mainNumber)

	print("\nLet's Play The mimsmind1 Game. You Have " + str(numberTries) + " Guesses.\n")

	StartGuessing(numberDigits, mainNumber, numberTries)

def StartGuessing(numberDigits, mainNumber, numberTries):
	userInput = ''
	userInputInt = 0
	userTries = 0
	numberBulls = 0
	numberCows = 0
	validInput = False
	firstInput = False

	while True:
		if(userTries < numberTries):
			try:
				if(not firstInput):
					userInput = input("Guess A " + str(numberDigits) + " Digit Number: ")
					firstInput = True
				else:
					if(validInput):
						userInput = input(str(numberBulls) + " bull(s), " + str(numberCows) + " cow(s). Try Again: ")
						numberBulls = 0
						numberCows = 0
					else:
						userInput = input("Invalid Number. Please Enter A " + str(numberDigits) + " Digit Number: ")
						numberBulls = 0
						numberCows = 0
				
				userInputInt = int(userInput)
				if(len(userInput) != numberDigits):
					raise ValueError
				else:
					userTries += 1
					validInput = True
			except ValueError:
				validInput = False
			finally:			
			# continuously ask for User Input and count the number of guesses it took to guess the right answer
				if(validInput):
					numberBulls = 0
					numberCows = 0
					if(userInput == mainNumber):
						print("Congratulations. You Have Guessed The Corrent Number In " + str(userTries) + " Tries.")
						return
					else:
						numberBulls, numberCows = GetCowsBulls(userInput, mainNumber)
		else:
			print("Sorry. You Did Not Guess The Number In " + str(numberTries) + " Tries. The Correct Number Is " + str(mainNumber) + ".")
			break

def GetCowsBulls(userInput, mainNumber):
	# this would return the number of bulls for the input given by the user
	numberBulls = 0
	numberCows = 0

	for n in range(len(str(userInput))):
		if(str(mainNumber)[n] == str(userInput)[n]):
			numberBulls += 1
		else:
			numberCows += CalcCows(str(userInput)[n], mainNumber)

	return numberBulls, numberCows

def CalcCows(userInputChar, mainNumber):
	# this would return 1 if the digit is present in the actual number

	if(str(mainNumber).find(userInputChar) >= 0):
		return 1

	return 0


def main():
	numberDigits = 3 # number of digits
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
				StartGame(numberDigits)
			return True
		except ValueError:
			print("\n*********************************************")
			print("Invalid User Input: " + str(sys.argv[1]) + ". Please Enter A Valid Positive Integer")
			return False

if __name__ == '__main__':
	main()
