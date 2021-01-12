#functions

def my_function():
    print("Hello")
    print("Bye")

my_function()

#KarelTheRobot
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

#Hurdles loop challenge
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def square():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()
    
def hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for i in range(0,6):
    hurdle()