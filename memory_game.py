import random
import time

def generate_sequence(difficulty):
    random_sequense = []
    for i in range(difficulty):
        number = random.randint(1,101)
        random_sequense.append(number)
    print(random_sequense,end="")
    time.sleep(3)
    print("\r     ")
    return random_sequense

def get_list_from_user():
    user_sequence = input(f"Please enter your sequence: \n")
    user_list = []
    for i in user_sequence.split():
        if i.isdigit():
            user_list.append(int(i))
        else:
            print("Input must include digits")
            return False
    print(f"List is: {user_list}")
    return user_list

def is_list_equal(user_list, random_sequense):
    # print(type(user_list[0]))
    print(len(random_sequense))

    if user_list == random_sequense:
        # print("Lists matches")
        return True
    else:
        print("List DO NOT match")
        return False
def play(difficulty):
    # difficulty = input("\nPlease chose difficulty level ")
    # if (difficulty.isdigit()) and int(difficulty) > 0:
        random_sequense = generate_sequence(difficulty)
        user_list = get_list_from_user()
        # print(f"user sequence is {user_list}")
        result = is_list_equal(user_list, random_sequense)
        # print(f"Result is: {result}")
        # if result == False:
        #     print("Wrong Guess")
        # else:
        #     pass
        return result







