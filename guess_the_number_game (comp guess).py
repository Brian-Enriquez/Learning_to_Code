from random import randint

#Guess the number game
#Computer is the guesser using randint from random

def computer_guess_the_number_game(x):
    low_guess = 1 #lowest possible guess
    high_guess = x #highest possible guess is based on user input of x
    user_feedback = '' #user inout will be a str
    while user_feedback != 'c': #enter while loop when not equal to 'c' str input is placed
        comp_guess = randint(low_guess, high_guess) #computer guesses a random number using randint
        user_feedback = input(f'Is {comp_guess} too high (h), too low (l), or correct (c)') #ask user for feedback about guessed number
        if user_feedback == 'h': #if guessed number is high replace high guess number with guessed number
            high_guess = comp_guess - 1
        elif user_feedback == 'l': #if guessed number is low replace low quess with guessed number
            low_guess = comp_guess + 1
    print(f'Your secret number is {comp_guess}, thank you for playing.') #exit while loop if guessed number is correct

computer_guess_the_number_game(100) #run the game with any user inputed x
                              
