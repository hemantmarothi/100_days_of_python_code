import random
user_choice=int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors: "))
if user_choice==2:
  print('''
      _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
elif user_choice==1:
  print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
elif user_choice==0:
  print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
else:
  print("incorrect choice")

comp_choice=random.randint(0,2)
print("Computer choose:-")
if comp_choice==2:
  print('''
      _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
elif comp_choice==1:
  print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
else:
  print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

if user_choice==0:
  if comp_choice==0:
    print("Draw")
  elif comp_choice==1:
    print("You lose")
  else:
    print("You win")
elif user_choice==1:
  if comp_choice==1:
    print("Draw")
  elif comp_choice==3:
    print("You lose")
  else:
    print("You win")
elif user_choice==2:
  if comp_choice==2:
    print("Draw")
  elif comp_choice==0:
    print("You lose")
  else:
    print("You win")