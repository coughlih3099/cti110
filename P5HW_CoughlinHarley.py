# this program adds or subtracts to random numbers between 1 and 300
# 11/15/2023
# CTI-110 P5HW - Math Quiz
# Harley Coughlin
#

import random

def check(user_input, answer):
  if (user_input < answer):
    print("Sorry, guess is too low.")
    return True
  elif (user_input == answer):
    print("Congratulations!!!! Your answer is correct.")
    return False
  elif (user_input > answer):
    print("Sorry, guess is too high.")
    return True


def addition():
  num1 = random.randint(1, 300)
  num2 = random.randint(1, 300)
  summed = num1 + num2

  print(f"{num1:>5}\n+ {num2:>3}\n\n")

  num_guesses = 0
  retry = True
  while (retry):
    if num_guesses == 0:
      user_input = int(input("Enter answer: "))
    else:
      user_input = int(input("Try again: "))

    num_guesses += 1
    retry = check(user_input, summed)
    continue
  
  print(f"Number of guesses: {num_guesses}\n")



def subtraction():

  num1 = random.randint(1, 300)
  num2 = random.randint(1, 300)
  subtracted = num1 - num2

  print(f"{num1:>5}\n- {num2:>3}\n\n")
  
  num_guesses = 0
  retry = True
  while (retry):
    if num_guesses == 0:
      user_input = int(input("Enter answer: "))
    else:
      user_input = int(input("Try again: "))

    num_guesses += 1
    retry = check(user_input, subtracted)
    continue
  
  print(f"Number of guesses: {num_guesses}\n")

if __name__ == '__main__':
  print("Welcome to Math Quiz\n\n\n\n")

  keep_going = True
  while (keep_going):
    print("MAIN MENU")
    print("-----------------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit\n")
    
    option = int(input("Please choose one of the menu options: "))

    if (option == 1):
      addition()
    elif (option == 2):
      subtraction()
    elif (option == 3):
      print("Thank you for playing")
      keep_going = False
    else:
      print("Please enter a valid choice.\n")
      continue