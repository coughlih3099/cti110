import random
import check

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
    retry = check.check(user_input, subtracted)
    continue
  
  print(f"Number of guesses: {num_guesses}\n")
