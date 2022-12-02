import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

player = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if player >= 3 or player < 0:
    print("You didn't follow directions so you are a loser!")
else:
    print(choices[player])

    computer = random.randint(0, 2)
    print("Computer chose:")
    print(choices[computer])

    if player == 0 and computer == 2:
        print("You're a winner! Keep it up!")
    elif computer == 0 and player == 2:
        print("Guess what, you're a loser..")
    elif computer > player:
        print("Ultimate loser..")
    elif player > computer:
        print("Congrats, you beat a computer!")
    elif player == computer:
        print("Picked the same, it's a draw")
