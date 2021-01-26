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

#Hurdle 2, random flag

while at_goal() != 1:
    hurdle()

#Hurdle 2, Random flag facit
while not at_goal():
    hurdle()

#Hurdle 3, Random Wall placement
def hurdle2():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        hurdle2()
    elif front_is_clear():
        move()

#Hurdle 4, Variable Height hurdle
def hurdle_top():
    turn_right()
    move()
    turn_right()
    move()

while not at_goal():
    if wall_in_front():
        turn_left()
        while wall_on_right() and front_is_clear():
            if at_goal() != 1:
                move()
        if right_is_clear():
            hurdle_top()
    elif front_is_clear:
        move()
    else:
        turn_left()

#Reeborg Maze

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif wall_on_right() and front_is_clear():
        move()
    else:
        turn_left()