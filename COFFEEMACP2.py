#2nd Method To do the Coffee machine problem
MENU = {
  "espresso": {
      "ingredients": {
          "water": 50,
          "coffee": 18,
      },
      "cost": 1.5,
  },
  "latte": {
      "ingredients": {
          "water": 200,
          "milk": 150,
          "coffee": 24,
      },
      "cost": 2.5,
  },
  "cappuccino": {
      "ingredients": {
          "water": 250,
          "milk": 100,
          "coffee": 24,
      },
      "cost": 3.0,
  }
}
resources = {
  "water": 300,
  "milk": 200,
  "coffee": 100,
}
tot = 0

def report():
  print(f"Items available along with their costs:")
  for i in MENU:
      print(f"{i} - ${MENU[i]['cost']}")
  print(f"Resources available:")
  for resource, amount in resources.items():
      print(f"{resource.capitalize()}: {amount}ml")

def check_available(choice):
  if choice == 1:
      drink = 'espresso'
  elif choice == 2:
      drink = 'latte'
  elif choice == 3:
      drink = 'cappuccino'

  for ingredient, required in MENU[drink]["ingredients"].items():
      if resources[ingredient] < required:
          print(f"Sorry, there is not enough {ingredient} for {drink}.")
          return False
  return True

def update_ingredients(choice):
  if choice == 1:
      drink = 'espresso'
  elif choice == 2:
      drink = 'latte'
  elif choice == 3:
      drink = 'cappuccino'

  for ingredient, required in MENU[drink]["ingredients"].items():
      resources[ingredient] -= required

def process_coins(choice):
  quarters = int(input("Enter the number of quarters: "))
  dimes = int(input("Enter the number of dimes: "))
  nickels = int(input("Enter the number of nickels: "))
  pennies = int(input("Enter the number of pennies: "))
  global tot
  tot = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

  if choice == 1 and tot >= 1.5:
      update_ingredients(choice)
      print("Enjoy your Espresso!!")
      print(f"Here is your change: ${round(tot - 1.5, 2)}")
  elif choice == 2 and tot >= 2.5:
      update_ingredients(choice)
      print("Enjoy your Latte!!")
      print(f"Here is your change: ${round(tot - 2.5, 2)}")
  elif choice == 3 and tot >= 3.0:
      update_ingredients(choice)
      print("Enjoy your Cappuccino!!")
      print(f"Here is your change: ${round(tot - 3.0, 2)}")
  else:
      print("Sorry! Not enough money!")

def choice_made(choice):
  if check_available(choice):
      process_coins(choice)
  else:
      print("Please choose another drink.")

while True:
  print("COFFEE TIME!! Espresso-$1.5  Latte-$2.5 Cappuccino-$3!\n")
  report()
  choice = int(input("What would you like to have? Enter 1 for Espresso, 2 for Latte, 3 for Cappuccino: "))
  if choice in [1, 2, 3]:
      choice_made(choice)
  else:
      print("Invalid choice.")

  c = input("Do you want to buy another coffee? 'Y' or 'N': ")
  if c.lower() != 'y':
      break
