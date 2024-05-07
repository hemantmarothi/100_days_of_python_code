#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

logo = """
  __ _ _   _  ___  ___ ___ 
 / _` | | | |/ _ \/ __/ __|
| (_| | |_| |  __/\__ \__ 
 \__, |\__,_|\___||___/___/
  __/ |                    
 |___/
 """
from random import randint
def main():
    game = True
    while game:
        print(logo)
        num = randint(1, 100)
        print(num)
        difficulty = input("Enter the Difficulty level (Type 'easy' or 'hard) (By Default: easy)").lower()
        num_guess = 5 if difficulty=="hard" else 10
        for i in range(num_guess):
            guess = int(input("Enter Your Guess: "))
            if guess==num:
                print("You Cracked It!")
                break
            elif(num < guess):
                print("Guess is too high")
            else:
                print("Guess is too low")
        else:
            print("You failed to guess")
        game = True if input("Type 0 to exit and 1 to play again")=="1" else False

main()