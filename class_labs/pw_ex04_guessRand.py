#pw_ex04_guessRand.py;
#depencancies: random, math;
#last edit: 2020-05-27, by pWurster;
#A standard number guessing game demo
#

import random
import math

#init vars
MAXNUMBER: int = 100 #alter this constant to change the difficulty
computerPick: int #will be randomized
userGuess: int #input from user
guessCounter: int = 1 #self explanatory

#assign random number from 1-MAXNUMBER to as computer's secret number
computerPick = random.randrange(1, MAXNUMBER + 1)

#prompt user to guess the computer's number
print(f'I have chosen a number between 1 and {MAXNUMBER}.\n')
userGuess = int(input('What do you think it is? '))

#loop until the guess is correct
while userGuess != computerPick:
        #use log2(n) to determine optimal number of guesses
	if guessCounter == math.ceil(math.log2(MAXNUMBER)):
                #encourage smarter play since user is making too many errors
		print('\nIf you had implemented a binary search pattern you would\'ve\ngotten it by now\n')

	#notify & re-prompt user
	print(f'Too {"high" if userGuess > computerPick else "low"}', end = '... ')
	userGuess = int(input('guess again: '))

        #increment counter
	guessCounter += 1

#reveal computer's secret number and the number of attempts
print(f'\nRight, my number was {computerPick}, it took you {guessCounter} attempt{"" if guessCounter == 1 else "s"}.')

