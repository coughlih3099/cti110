#takes two arguments and returns if the answer is the same as input

def check(user_input, answer):
    if (user_input < answer):
        print("Sorry, guess is too low.\n")
        return True
    elif (user_input == answer):
        print("Congratulations!!!! Your answer is correct.\n")
        return False
    elif (user_input > answer):
        print("Sorry, guess is too high.\n")
        return True
