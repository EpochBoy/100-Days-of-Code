
for number in range(1, 101):
# Changed if state from or to and since both conditions must resolve to true
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
# Changed the if to elif
  elif number % 3 == 0:
    print("Fizz")
# Changed the if to elif
  elif number % 5 == 0:
    print("Buzz")
  else:
# Changed [number] to number for a cleaner look
    print(number)