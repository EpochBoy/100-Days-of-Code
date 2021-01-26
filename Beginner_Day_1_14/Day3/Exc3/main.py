# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# #Checking if math checks out
# #If year is evenly divisible by 4
# if (year/4).is_integer():
#     print("Is leap")
# else:
#     print("Is not leap")
# #Except every year that is evenly divisible by 100
# if (year/100) % 2 == 0:
#     print("Is not leap")
# else:
#     print("Is not leap")
# #Unless the year is also evenly divisible by 400
# if (year/400).is_integer():
#     print("Is leap")
# else:
#     print("Is not leap")

#Wrapping it into a proper statement
if (year/4).is_integer() and (year/100)%2==0 and (year/400).is_integer():
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

#Facit Solution
if year % 4 == 0:
    if year % 100:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not leap year")
    else:
        print("Leap Year")
else:
    print("Not leap year.")