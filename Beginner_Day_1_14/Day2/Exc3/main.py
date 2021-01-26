# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_int = int(age)

Total_Days = 365*90
Total_Weeks = 52*90
Total_Months = 12*90

Age_in_Days = age_int*365
Age_in_Weeks = age_int*52
Age_in_Months = age_int*12

Remaining_Days = Total_Days-Age_in_Days
Remaining_Weeks = Total_Weeks-Age_in_Weeks
Remaining_Months = Total_Months-Age_in_Months

print(f"You have {Remaining_Days} days, {Remaining_Weeks} weeks and {Remaining_Months} months left in your life if you make it to 90")