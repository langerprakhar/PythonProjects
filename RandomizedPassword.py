#PASSWORD GENERATOR WHICH IS RANDOMIZED AS WELL AS ORDERED IF YOU WANT
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

list=[letters,numbers,symbols]
password=""

for l in list:
  choice=input("What do you want to choose? Type 'L' for letters, 'S' for symbols and 'N' for numbers\n")
  if(choice=='L' or choice=='l'):
    nr_letters= int(input("How many letters would you like in your password?\n"))
    for i in range(0,nr_letters):
      password+=random.choice(letters)
  elif(choice=='S' or choice=='s'):
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    for j in range(0,nr_symbols):
      password+=random.choice(symbols)
  elif(choice=='N' or choice=='n'):
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    for k in range(0,nr_numbers):
       password+=random.choice(numbers)
  else:
    print("Invalid choice try again!!")
print(f"Password in random form of letters,symbols and numbers is:{password}")