#Write your code below this row 👇

even_sum = 0

for number in range(1,101):
    if number%2 == 0:
        even_sum+=number
print(even_sum)

#Facit

total = 0
for number in range(2,101,2):
    total+=number
print(total)
