import random
import requests

def play(difficulty):
    # difficulty = input("\nPlease chose difficulty level ")
    # if (difficulty.isdigit()) and int(difficulty) > 0:
    #     print(f"Difficulty is valiud and equal to: {difficulty}")
    #     return difficulty
    #     # pass
    # else:
    #     print(f"\nwrong difficulty level {difficulty}")
    #     exit(1)
    # x = play()
    # print(f"difficulty is: {difficulty}")
    x = difficulty
    ils_rate = get_money_interval()
    # print(f"ILS rate is: {ils_rate}")
    guess = get_guess_from_user()
    # print(f"Guess of the user is: {guess}")
    guess_in_ils = guess[0]
    # print(f"guess in ils is: {guess_in_ils}")
    usd_amount = guess[1]
    # print(f"USD amout is: {usd_amount}")
    result = is_list_equal(guess_in_ils, usd_amount, ils_rate, x)
    # print(f"result is {result}")
    return result

def get_money_interval():
    url = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd/ils.json'
    response = requests.get(url)
    data = response.json()
    # print(data)
    ils_rate = data["ils"]
    return ils_rate

def get_guess_from_user():
    usd_amount = random.randint(1, 100)
    guess_in_ils = input(f"\nWhat is the rate of {usd_amount} USD in ILS ? ")
    return guess_in_ils , usd_amount


def is_list_equal(guess_in_ils, usd_amount, ils_rate, x):
    if int(guess_in_ils) < int(usd_amount)*float(ils_rate)+10-x and int(guess_in_ils) > int(usd_amount)*float(ils_rate)-10+x:
        # print("within range")
        return True
    else:
        # print("wrong guess")
        return False


