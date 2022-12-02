print(
    '''
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
'''
)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = (
    input("You're on Treasure Island, do you go left or right?\n")).lower()
water = ""
door = ""

if direction == "left":
    water = (input("You see run into a body of water, do you swim or wait?\n")).lower()
    if water == "wait":
        door = (
            input(
                "Miraculously a boat comes your way and takes you to a building with three doors. Which door do you choose? Red, green, or blue?\n"
            )
        ).lower()
        if door == "yellow":
            print("Congratulations, you found the treasure, but it is haunted!")
        elif door == "red":
            print("Game over. Behind the red door was a killer clown. You dead.")
        elif door == "blue":
            print(
                "Game over. The blue door took you to a locked room that's playing Nickelback 24/7. Sorry"
            )
        else:
            print("Game over. You have choosen poorly.")
    elif water == "swim":
        print("Game over. A great white shark swoops in and eats you. Ouch.")
    else:
        print("Game over. You have choosen poorly.")
elif direction == "right":
    print(
        "Game over. You run into a local tribe and they kill you where you stand. Sorry"
    )
else:
    print("Game over. You have choosen poorly.")
