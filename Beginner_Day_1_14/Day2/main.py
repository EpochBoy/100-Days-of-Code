# #Basic Data types

# #String
# #This method of pulling out a char from String is called Subscripting
# print("Hello"[4])

# print("123"+"456")

# #Integer
# print(123+456)

# #Delimiters
# print(123_456_789)

# #Float
# print(3.14159)

# #Boolean
# print(True)
# print(False)

# num_char = len(input("What is your name? "))

# #checking var type
# print(type(num_char))

# #typecasting
# new_num_char = str(num_char)

# #Now no typeclashing
# print("Your name has "+new_num_char+" characters")

# a = str(123)
# print(type(a))


#Mathematical Operators
# 3+5
# 7-4
# 3*2
# 6/3
#Exponent
# print(2**4)

#Priority: PEMDAS
# Parentheses
# Exponents
# Multiplication
# Division
# Addition
# Substraction

# print(3*(3+3)/3-3)

#Rounding

# print(8/3)

# #Just cuts off the decimals
# print(int(8/3))

# #Respects .4 - .5 math rule
# print(round(8/3))

# #Rounding to a decimal point
# print(round(8/3, 2))

# Floor Division, automatically converts to an integer
# print(8//3)

#Shorthands += -= *= /=

#f-String
score=4
height = 1.87
isWinning = True

print(f"your score is {score} and your height is {height} and your are winning? {isWinning}")

