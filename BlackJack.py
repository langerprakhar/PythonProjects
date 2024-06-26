#BlackJack Game!!
#Use of all the things that have been done till now!
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
logo = """
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/
"""

def call():
  print(logo)
  def deal_card():
    """Returns a random card from the deck!"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

  def calculate_score(cards):
    #use of sum function in python to calculate sum of the elements     in the list
    if len(cards)==2 and sum(cards)==21:
      return 0

    if 11 in cards and sum(cards)>21:
      cards.remove(11)
      cards.append(1)
    return(sum(cards))
  def compare(user_score,computer_score):
    if user_score==computer_score:
      return "Draw!!"
    elif computer_score==0:
      return "Lose.Opponent has BlackJack"
    elif user_score==0:
      return "Win with a BlackJack!!"
    elif user_score>21:
      return "You went over 21 you lose!"
    elif computer_score>21:
      return "You win the computer went over 21!!"
    elif user_score>computer_score:
      return "You win"
    else:
      return "You lose!"
  user_cards=[]
  computer_cards=[]
  is_gameover=False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  #for the user
  while is_gameover is False:
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f"Your cards:{user_cards}, current score:{user_score}")
    print(f"Computer's first card:{computer_cards[0]}")

    if user_score==0 or computer_score==0 or user_score>21:
      is_gameover=True
    else:
      user_should_deal=input("Type 'y' to get another card and 'n' to pass:")
      if user_should_deal== 'y':
        user_cards.append(deal_card())
      else:
        is_gameover=True

  #for the computer
  while computer_score !=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)

  print(f"Your final hand:{user_cards} and your score was :{user_score}")
  print(f"Computer's final hand:{computer_cards} and computer's score was:{computer_score}")
  print(compare(user_score,computer_score))

while input("Do you wanna play a game of BlackJack? Type 'y' or 'n':")=='y':
  clear()
  call()
print("Why did you come here in the first place if you didnt wanna play dumbo")