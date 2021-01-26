# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
name = input("What's your name? ")
location = input("Where are you from? ")

def greet(name, location):
    print(f"Hello Mr.{name}")
    print(f"{location} is a nice place!")

greet(name, location)


#Keyword arguments, avoid sequential params
greet(location=location, name=name)

