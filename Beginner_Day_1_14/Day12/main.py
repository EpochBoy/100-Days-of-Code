################### Scope ####################

enemies = 2

def increase_enemies():
    # Bad form to change global variables from within local
    # global enemies
    # enemies = 1
    print(f"enemies inside function: {enemies}")
    # instead use return statement to manipulate 
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
# drink_potion()
# print(potion_strength)

# Global Scope
# player_health = 10
# def game():
#     #drink_potion is no a local scope function
#     def drink_potion():
#         # This is a local variable
#         potion_strength = 2
#         # This is printing the Global variable
#         print(player_health)
#     #Calling drink_potion() from within local scope and calling game() in global scope
#     drink_potion()

# # Can no longer call drink_potion, since it's now local scope in game()
# # drink_potion()
# game()

# # There is no Block Scope
# game_level = 3
# enemies = ["Skeles", "Beasts", "Alien"]

# if game_level < 5:
#     new_enemy = enemies[0]

# #Variable instantiated in if statement is still Global
# print(new_enemy)

#Global Constants
#Naming convention in Python is all upper case for CONSTANTS
PI = 3.14159
URL = "http://www.google.compile"

def calc():
    return PI

calc
