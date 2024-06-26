#Rock paper scissors shooottt!!!
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
comp=[rock,paper,scissors]
comp_random_choice=random.randint(0,2)

choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if(choice>=3 or choice<0):
  print("Invalid choice select again!!")
else:
  print("You chose:")
  print(comp[choice])
  print("Computer chose:")
  print(comp[comp_random_choice])
  if choice==comp_random_choice:
    print("It's a draw")
  elif (choice==0 and comp_random_choice==2) or (choice==2 and comp_random_choice==1) or (choice==1 and comp_random_choice==0):
    print("You win")
  else:
    print("Computer won!!")