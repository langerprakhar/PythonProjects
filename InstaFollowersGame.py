#Higher Lower Game Insta followers based
import random
from game_data import data
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

logo = """
    __  ___       __
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /
/_/ ///_/\__, /_/ /_/\___/_/
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /
/_____/\____/|__/|__/\___/_/
"""

vs = """
 _    __
| |  / /____
| | / / ___/
| |/ (__  )
|___/____(_)
"""
random_choice = random.choice(data)
random_choice1 = random.choice(data)
k = 0

def printA():
    print(
        f"Compare A:{random_choice['name']}, who is a {random_choice['description']} ,from {random_choice['country']}"
    )

def printB():
    print(
        f"Compare B:{random_choice1['name']}, who is a {random_choice1['description']} ,from {random_choice1['country']}"
    )

def randomPrintA():
    random_choice = random.choice(data)
    print(
        f"Compare A:{random_choice['name']}, who is a {random_choice['description']} ,from {random_choice['country']}"
    )

def randomPrintB():
    random_choice1 = random.choice(data)
    print(
        f"Compare B:{random_choice1['name']}, who is a {random_choice1['description']} ,from {random_choice1['country']}"
    )

def choose():
    global k
    bool = True
    print(logo)
    printA()
    print(vs)
    printB()
    while bool:
        choice = input("Who do you think has more followers A or B?:")
        if choice == 'A' or choice == 'a':
            if random_choice['follower_count'] > random_choice1[
                    'follower_count']:
                k += 1
                clear()
                print(logo)
                print(f" You guessed it right!Your Current score is {k}")
                printA()
                print(vs)
                randomPrintB()
                continue
            elif random_choice['follower_count'] < random_choice1[
                    'follower_count']:
                clear()
                print(logo)
                print("Sorry!!You lost!")
                print(f"Your final Score was:{k}")
        elif choice == 'B' or choice == 'b':
            if random_choice['follower_count'] < random_choice1[
                    'follower_count']:
                k += 1
                clear()
                print(logo)
                print(f" You guessed it right!Your Current score is {k}")
                randomPrintA()
                print(vs)
                printB()
                continue
            elif random_choice['follower_count'] > random_choice1[
                    'follower_count']:
                clear()
                print(logo)
                print("Sorry!!You lost!")
                print(f"Your final Score was:{k}")
                break
choose()
