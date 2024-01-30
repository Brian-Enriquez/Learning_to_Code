import tkinter
import random

#Guess the number game but instead of using console a popup window is used for input
#Provides a separate window for user to play the game

random_number = random.randint(1, 100)  # random number will be generated from the provided range

def guess_number_game():  # x will determine the range of numbers for the game
    try:
        user_guess = int(entry.get())  # initial user variable
        #while user_guess != random_number:  # enter loop while the user_guess is too high or too low
            #user_guess = int(input(f'Please select a number from 1 to 100:'))  # ask user for user input
        if user_guess < random_number:
            result_label.config(text="Sorry, try again the guessed number is too low")  # if less than random_number print
        elif user_guess > random_number:
            result_label.config(text="Sorry, try again the guessed number is too high")  # if greater than random_number print
        else:
            result_label.config(text=f"Congratulations, you were able to guess the random number:{random_number}")  # User guesses number print
    except ValueError:
        result_label.config(text="Invalid input. Only numbers allowed.") #if the value entered is not a integer then request for an integer

window = tkinter.Tk() #open a popup window
window.title("UI") #title the window which is a user interface
label = tkinter.Label(window, text="Guess the Number").pack() #insert a label to provide information
window.geometry("200x100")
entry = tkinter.Entry(window, width=20) #entry line for user to input numbers
entry.pack()
result_label = tkinter.Label(window, text="") #result label to collect the information from the function
result_label.pack()
button = tkinter.Button(window, text="Guess", command=guess_number_game) #guess button to confirm user input and run function guess_the_number
button.pack()

window.mainloop()



