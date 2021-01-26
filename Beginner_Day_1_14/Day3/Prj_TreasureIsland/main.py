print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

xroad = input("You're at a xroad, do you want to go left or right? Type left or right\n").lower()
if xroad == "left":
    print("You are indeed an experienced adventurer!\n")
    lake = input("You've now come to a lake, want to swim across or go around it? Type swim or around\n").lower()
    if lake == "around":
        print("You are tired af the long walk, but it seems your choice was a good one.\n")
        print("You spotted several crocodiles in the lake during your walk\n")
        print("You've arrived at the castle, how will this challenge be tackled?\n")
        print("It seems you have several choices. A red door, a blue door or the yellow door\n")
    else:
        print("You are devoured by hungry crocodiles! Poor Boo, who will save him now?")
        exit()
    door = input("Type red, blue or yellow, to pick a door\n").lower()
    if door == "yellow":
        print("Congratulations Minsc, you've saved Boo")
    elif door == "red":
        print("Poor Minsc, you've been burned to a crisp")
    elif door == "blue":
        print("Irenicus transforms Boo into a dragon, that kills you")
else:
    print("What a poor choice you've made. You are now DEAD")



#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload