#HANGMAN GAME!!
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
hangman_words = [
    "apple", "banana", "grape", "orange", "pear", "peach", "melon", "berry", "kiwi", "plum",
    "dog", "cat", "fish", "bird", "horse", "mouse", "rat", "cow", "pig", "goat",
    "car", "bus", "bike", "train", "plane", "boat", "truck", "van", "jeep", "taxi",
    "red", "blue", "green", "yellow", "black", "white", "purple", "pink", "brown", "gray",
    "hat", "shirt", "pants", "shoes", "dress", "coat", "scarf", "gloves", "socks", "boots",
    "home", "school", "park", "store", "library", "beach", "pool", "garden", "house", "office",
    "happy", "sad", "angry", "excited", "bored", "tired", "scared", "nervous", "proud", "calm",
    "run", "jump", "walk", "swim", "read", "write", "draw", "sing", "dance", "play",
    "pizza", "pasta", "bread", "rice", "soup", "salad", "cake", "cookie", "fruit", "cheese",
    "summer", "winter", "spring", "fall", "rain", "snow", "wind", "sun", "cloud", "storm"
]
logo = '''
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print(logo)
lives=6
chosen_word=random.choice(hangman_words)

display=[]
for i in chosen_word:
    display+='_'

bool=True
while bool:
    guess=input("Guess a letter:").lower()
    clear()
    if guess in display:
        print("Letter already guessed!")
    for index in range(len(chosen_word)):
            if chosen_word[index]==guess:
                display[index]=guess
    if guess not in chosen_word:
        print("You lose a life")
        lives-=1
        if lives==0:
            bool=False
            print("You lose!")
            print(f"The word was {chosen_word}")
    print(f"{' '.join(display)}")
    j=0
    for index in range(len(display)):
        if display[index]==chosen_word[index]:
            j+=1
    if j==len(chosen_word):
        print("You won")
        break

    print(stages[lives])