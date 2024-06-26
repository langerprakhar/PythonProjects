#NUMBER GUESSING WITH 2 LEVELS EASY AND HARD

def easy_lvl():
  k=10
  print(f"You have {k} attempts to guess the number!")
  while True:
    guess=int(input("Make a Guess:"))
    if guess>random_number:
      print("Too High!")
      print("Guess Again!")
      k-=1
      if k==0:
        print("You lose!")
        break
      else:
        print(f"You have {k} attempts remaining")
    elif guess<random_number:
      print("Too low!")
      print("Guess Again!")
      k-=1
      if k==0:
        print("You lose!")
        break
      else:
        print(f"You have {k} attempts remaining")

    elif guess==random_number :
      print(f"You guessed it the number was {guess}")
      break

def hard_lvl():
  k=5
  print(f"You have {k} attempts to guess the number!")
  while True:
    guess=int(input("Make a Guess:"))
    if guess>random_number:
      print("Too High!")
      print("Guess Again!")
      k-=1
      if k==0:
        print("You lose!")
        break
      else:
        print(f"You have {k} attempts remaining")
    elif guess<random_number:
      print("Too low!")
      print("Guess Again!")
      k-=1
      if k==0:
        print("You lose!")
        break
      else:
        print(f"You have {k} attempts remaining")

    elif guess==random_number :
      print(f"You guessed it the number was {guess}")
      break
  
import random
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|
"""
print(logo)
print("Welcome to the Number guessing Game!!")
print("I'm thinking of a number between 1 and 100")
choice=int(input("Choose a level:'easy' or 'hard','1' for easy and '2' for hard!"))
random_number=random.randint(0,100)
if choice==1:
  easy_lvl()
elif choice==2:
  hard_lvl()