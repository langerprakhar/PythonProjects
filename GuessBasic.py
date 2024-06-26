#Number guessing game
import random

print("NUMBER GUESSING GAME!")
n = random.randint(1, 10)

while True:
    num = int(input("Enter the number between 1 and 10: "))
    if num == n:
        print(f"You guessed it correctly! The number was {n}")
        break
    elif num > n:
        print("Too High")
    else:
        print("Too Low")