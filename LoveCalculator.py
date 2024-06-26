print("The Love Calculator is calculating your score...")
name1 = input("What is your name?") # What is your name?
name2 = input("What is their name?") # 

low1=name1.lower()
low2=name2.lower()
t=low1.count("t")+low2.count("t")
r=low1.count("r")+low2.count("r")
u=low1.count("u")+low2.count("u")
e=low1.count("e")+low2.count("e")
l=low1.count("l")+low2.count("l")
o=low1.count("o")+low2.count("o")
v=low1.count("v")+low2.count("v")
e=low1.count("e")+low2.count("e")

true=t+r+u+e
love=l+o+v+e
score=str(true)+str(love)

if score<'10' or score>'90':
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >='40' and score<='90':
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")