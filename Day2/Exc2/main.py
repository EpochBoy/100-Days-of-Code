# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#My Solution
print(int(float(weight)/(float(height)*float(height))))

#Facit

bmi = int(weight) / float(height)**2

print(int(bmi))