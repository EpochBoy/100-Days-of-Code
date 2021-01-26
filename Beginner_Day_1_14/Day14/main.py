from art import logo, vs
from game_data import data
import random
import os

def picker():
    choice = data[random.randint(0, len(data)-1)]
    name = choice.get("name")
    followers = int(choice.get("follower_count"))
    description = choice.get("description")
    country = choice.get("country")
    return name, followers, description, country

def printer(name1, name2, description1, description2, country1, country2, logo, vs):
    print(logo)
    print(f"Compare A: {name1}, a {description1}, from {country1}")
    print(vs)
    print(f"Compare B: {name2}, a {description2}, from {country2}")

def choose(followers1, followers2):
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_choice == "a":
        if followers1 >= followers2:
            return True
        elif followers1 < followers2:
            return False
    if user_choice == "b":
        if followers2 >= followers1:
            return True
        elif followers2 < followers1:
            return False

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

game_state = True
def runner(logo, vs, game_state):
    score = 0
    while game_state == True:
        name2, followers2, description2, country2 = picker()
        name1, followers1, description1, country1 = picker()
        while name1 == name2:
            name2, followers2, description2, country2 = picker()
        printer(name1, name2, description1, description2, country1, country2, logo, vs)
        choice = choose(followers1, followers2)
        if choice == True and followers1 == followers2:
            cls()
            print(f"They both have the same amount of followers")
        elif choice == True and followers1 != followers2:
            cls()
            score+=1
            print(f"You're right! Current score: {score}")
        elif choice == False:
            cls()
            print(f"Sorry you're wrong, your final score wasa: {score}")
            break

runner(logo, vs, game_state)