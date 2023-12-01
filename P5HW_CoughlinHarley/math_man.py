import random
import check

def math_man(choice):
    num1 = random.randint(1, 300)
    num2 = random.randint(1,300)
    
    if choice == 1:
        mathed = num1 + num2
        print(f"{num1:>5}\n+ {num2:>3}\n\n")
    else:
        mathed = num1 - num2
        print(f"{num1:>5}\n- {num2:>3}\n\n")

    num_guesses = 0
    retry = True
    while (retry):
        if num_guesses == 0:
            user_input = int(input("Enter answer: "))
            print()
        else:
            user_input = int(input("Try again: "))
            print()

        num_guesses += 1
        retry = check.check(user_input, mathed)
    
    print(f"Number of guesses: {num_guesses}\n")
