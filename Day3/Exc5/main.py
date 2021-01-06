# 🚨 Don't change the code below 👇
from typing import Counter


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Convert names to lower case
lower_name1 = name1.lower()
lower_name2 = name2.lower()


#Count TRUE
t=lower_name1.count('t')+lower_name2.count('t')
r=lower_name1.count('r')+lower_name2.count('r')
u=lower_name1.count('u')+lower_name2.count('u')
e=lower_name1.count('e')+lower_name2.count('e')

#Count LOVE
l=lower_name1.count('l')+lower_name2.count('l')
o=lower_name1.count('o')+lower_name2.count('o')
v=lower_name1.count('v')+lower_name2.count('v')
#E already counted in TRU>E<

#Dirty score calc
score = int(str(t+r+u+e)+str(l+o+v+e))

if score < 10 or score >= 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")
