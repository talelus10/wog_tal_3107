
import random

def generate_number(difficulty):
    secret_number = random.randint(1,difficulty)
    # print(f" secret number is {secret_number}")
    return secret_number

def get_guess_from_user():
    number_from_user = input("\n Please enter a number: ")
    if (number_from_user.isdigit()) and int(number_from_user) > 0:
        return number_from_user

def compare_results(secret, num_from_user):
    if int(secret) == int(num_from_user):
        # print("numbers equal")
        return True
    else:
        return False

def play(difficulty):
    # difficulty = input("\nPlease chose difficulty level ")
    # if (difficulty.isdigit()) and int(difficulty) > 0:
    #     pass
    # else:
    #     print(f"\nwrong difficulty level {difficulty}")
    #     exit(1)


    secret = generate_number(difficulty)
    # print(f"secret number is {secret}")
    num_from_user = get_guess_from_user()
    # print(f"Number from user is: {num_from_user}")
    is_equal = compare_results(secret, num_from_user)
    # print(f"Your guess is: {is_equal}")
    return is_equal


# play()
