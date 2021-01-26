#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random


#chosen_word = word_list[random.randint(0,len(word_list)-1)]

#facit
chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Please guess a letter from a-z: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# if guess in chosen_word:
#     print("you guessed right")

#facit
for letter in chosen_word:
    if letter == guess:
        print("You guessed right")
    else:
        print("You guessed wrong")
