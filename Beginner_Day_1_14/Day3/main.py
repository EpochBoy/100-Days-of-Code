#if else statements

# water_level = 90

# if water_level > 80:
#     print("Drain Water")
# else:
#     print("Fill bathtub")

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the coaster!")
# else:
#     print("Sorry, please come back when you've grown")

#Comparison Operators
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to
# != Not equal to

#Nesting if statements
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <= 55:
    print("Everything is going to be ok. Have a free ride on us!")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")


