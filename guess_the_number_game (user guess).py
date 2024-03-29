import random


#Guess the number game
#User has to guess the random number generated by the computer


def guess_number_game(x): #x will determine the range of numbers for the game
    random_number = random.randint(1, x) #random number will be generated from the provided range
    user_guess = 0 #initial user variable
    result = ''
    while user_guess != random_number: #enter loop while the user_guess is too high or too low
        user_guess = int(input(f'Please select a number from 1 to {x}:')) #ask user for user input
        if user_guess < random_number:
            result = print("Sorry, try again the guessed number is too low") #if less than random_number print
        if user_guess > random_number:
            result = print("Sorry, try again the guessed number is too high") #if greater than random_number print
    result = print(f'Congratulations, you were able to guess the random number: {random_number}') #User guesses number print

