"""
IMPORT
"""
import random 

number = random.randint(1,10)
isGuessCorrect = False

"""
PRINT
"""
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of the number, and you will do the guessing.")
print("Guess wrong and...")

while isGuessCorrect != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessCorrect = True
    else:
        print("You guessed {}. Sorry, that's not right... Keep trying.".format(guess))