#Coffee Machine Code
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
tot=0

changeW1=0
changeC1=0
changeW2=0
changeM2=0
changeC2=0
changeW3=0
changeM3=0
changeC3=0

def report():
  print(f"Items available along with their costs:")
  for i in MENU:
    print(f"{i}-${MENU[i]['cost']}")
  print(f"Ingredients available for Espresso!")
  print(f"{MENU['espresso']['ingredients']}")
  print(f"Ingredients available for Latte!")
  print(f"{MENU['latte']['ingredients']}")
  print(f"Ingredients available for Cappuccino!")
  print(f"{MENU['cappuccino']['ingredients']}")


def update_ingredients():
  
 if choice==1:
   global changeW1
   global changeC1
   changeW1=resources['water']-MENU['espresso']['ingredients']['water']
   changeC1=resources['coffee']-MENU['espresso']['ingredients']['coffee']
   resources['water']=changeW1
   resources['coffee']=changeC1
 elif choice==2:
   global changeW2
   global changeM2
   global changeC2
   changeW2=resources['water']-MENU['latte']['ingredients']['water']
   changeM2=resources['milk']-MENU['latte']['ingredients']['milk']
   changeC2=resources['coffee']-MENU['latte']['ingredients']['coffee']
   resources['water']=changeW2
   resources['milk']=changeM2
   resources['coffee']=changeC2
 elif choice==3:
    changeW3=resources['water']-MENU['cappuccino']['ingredients']['water']
    changeM3=resources['milk']-MENU['cappuccino']['ingredients']['milk']
    changeC3=resources['coffee']-MENU['cappuccino']['ingredients']['coffee']
    resources['water']=changeW3
    resources['milk']=changeM3
    resources['coffee']=changeC3


def process_coins():
  quarters=int(input("Enter the number of quarters:"))
  dimes=int(input("Enter the number of dimes:"))
  nickel=int(input("Enter the number of nickels:"))
  penny=int(input("Enter the number of pennies:"))
  global tot
  tot=(quarters*0.25)+(dimes*0.10)+(nickel*0.05)+(penny*0.01)
  if choice==1 and tot>=1.5:
    check_available()
    print("Enjoy your Espresso!!")
    print(f"Here is your change:{round((tot-1.5),2)}")
  elif choice==2 and tot>=2.5:
    check_available()
    print("Enjoy your Latte!!")
    print(f"Here is your change:{round((tot-2.5),2)}")
  elif choice==3 and tot>=3.0:
    check_available()
    print("Enjoy your Latte!!")
    print(f"Here is your change:{round((tot-3.0),2)}")
  elif tot<1.5:
    print("Sorry! Short of Money!!")


def check_available():
  if choice==1:
    if changeW1>=0:
      if changeC1>=0:
        print("Available!!")
        
  elif choice==2:
    if changeW2>=0:
      if changeM2>=0:
        if changeC2>=0:
          print("Available!!")
          
  elif choice==3:
    if changeW3>=0:
      if changeM3>=0:
        if changeC3>=0:
          print("Available!!")
          

def choice_made(choice):
  if choice==1:
    
    check_available()
    process_coins()
  elif choice==2:

    check_available()
    process_coins()
  elif choice==3:

    check_available()
    process_coins()
  else:
    print("Wrong choice")
while True:
  print("COFFEE TIME!! Espresso-$1.5  Latte-$2.5 Cappuccino-$3!\n")
  report()
  choice =int(input("What Would You Like To Have (Espresso/Latte/Cappuccino)? Enter 1 for Espresso 2 for Latte 3 for Cappuccino!:"))
  choice_made(choice)
  update_ingredients()
  c=input("Do you wanna buy another coffee?: 'Y' or 'N':")
  if c=='Y' or c=='y':
    
    continue
  else:
    break
