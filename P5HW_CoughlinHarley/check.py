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
