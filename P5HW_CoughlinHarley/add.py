import random
import check

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
