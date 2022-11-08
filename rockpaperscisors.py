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

#Write your code below this line 👇
#https://replit.com/@J3drek79/rock-paper-scissors-start#main.py
import random

humanchoice = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if humanchoice == 0:
  print(rock)
elif humanchoice == 1:
  print(paper)
else:
  print(scissors)
print("Computer choose:")
cpuchoice = random.randint(0, 2)
if cpuchoice == 0:
  print(rock)
elif cpuchoice == 1:
  print(paper)
else:
  print(scissors)
if humanchoice == cpuchoice:
  print("It's a draw")
elif humanchoice == 0 and cpuchoice == 1:
  print("You lose!")
elif humanchoice == 0 and cpuchoice == 2:
  print("You won!")
elif humanchoice == 1 and cpuchoice == 0:
  print("You won!")
elif humanchoice == 1 and cpuchoice == 2:
  print("You lose!")
elif humanchoice == 2 and cpuchoice == 0:
  print("You lose!")
else:
  print("You won!")
