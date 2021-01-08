# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

xguest = len(names)-1
picker = random.randint(0,xguest)
winnerwinnerchickendinner = names[picker]

print(f"{winnerwinnerchickendinner} is picking up todays bill!")

#Facit same

#Why random is exempt

print(random.choice(names))

