#Basic Data types

#String
#This method of pulling out a char from String is called Subscripting
print("Hello"[4])

print("123"+"456")

#Integer
print(123+456)

#Delimiters
print(123_456_789)

#Float
print(3.14159)

#Boolean
print(True)
print(False)

num_char = len(input("What is your name? "))

#checking var type
print(type(num_char))

#typecasting
new_num_char = str(num_char)

#Now no typeclashing
print("Your name has "+new_num_char+" characters")

a = str(123)
print(type(a))