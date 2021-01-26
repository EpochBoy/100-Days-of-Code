#Number Guessing Game Objectives:
# Include an ASCII art logo.
# http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

player_guesses = 0
number_to_guess = 0

def number_guesser():
    return number_to_guess + random.randint(1,100)

#Difficulty Selector
def diff():
    print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input(print("Choose a difficulty. Type 'easy' or 'hard': "))
    if difficulty == "easy":
        print("You start with 10 lives")
        return player_guesses+10
    elif difficulty == "hard":
        print("You start with 5 lives")
        return player_guesses+5
    else:
        print("Not an option")
        exit()

#Game
game_state = True
def number_game(game_state):
    player_guesses = diff()
    number_to_guess = number_guesser()
    while game_state == True:
        player_input = int(input("What is your guess? "))
        player_guesses = player_guesses-1
        if player_guesses == 0:
            print("You have no more lives left")
            try_again = input("Do you want to try again 'y' 'n'?: ")
            if try_again == "y":
                number_game()
            elif try_again == "n":
                return game_state+False
        elif player_guesses > 0:
            if player_input > number_to_guess:
                print("Too high!")
                print(f"Guess left: {player_guesses}")
            elif player_input < number_to_guess:
                print("Too low.")
                print(f"Guess left: {player_guesses}")
            elif player_input == number_to_guess:
                print("Well done! You guessed the number")
                try_again = input("Do you want to try again 'y' 'n'?: ")
                if try_again == "y":
                    number_game()
                elif try_again == "n":
                    return game_state+False
number_game(game_state=game_state)