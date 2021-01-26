############DEBUGGING#####################

# Describe Problem
# def my_function():
# #   for i in range(1, 20):
# # If you want to print i == 20, range has to be (1,21)
#     for i in range(1,21):
#         if i == 20:
#             print("You got it")
# my_function()

# # Reproduce the Bug
# Randint should be (0,5), list is 0 indexed
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# # dice_num = randint(1, 6)
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer
# Should be >= or <= to include the starting years of mentioned generation
# year = int(input("What's your year of birth?"))
# if year >= 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# added cast input to int
# age = int(input("How old are you?"))
# if age > 18:
#     # Added f string + indent for print statement
#     print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# Removed an = to make it assign the value correctly instead of compare
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# Indent error, b_list should be within scope of the for loop
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])