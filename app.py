



# from currency_roulette_game import *
# from memory_game import *
from score import add_score

def welcome():
    person_name = input("Please enter your name: ")
    print(f"\nHi {person_name} and welcome to the World of Games: The Epic Journey\n")
    # return (person_name)

def start_play():

    list_of_games = {
        "1": "Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.",
        "2": "Guess Game - guess a number and see if you chose like the computer.",
        "3": "Currency Roulette - try and guess the value of a random amount of USD in ILS"
    }
    # print(list_of_games)
    for i in list_of_games:
        print(f"{i}. {list_of_games[i]}")
    get_game_number = input("\nPlease chose number of the game to play: ")

    if get_game_number.isdigit():
        get_game_number = int(get_game_number)
    else:
        print("Not a number")
        return False
    # print(f"chosen game is: {list_of_games[get_game_number]}")

    # if get_game_number != 1 and get_game_number != 2 and get_game_number != 3:
    if get_game_number in [1, 2, 3]:
        pass
    else:
        print("Invalid Game Number - Please chose again!!!")
        return False

        # return (get_game_number)

    difficulty_levels = [1, 2, 3, 4, 5]
    difficulty = input("\nselect a difficulty level between 1 and 5: ")

    if (difficulty.isdigit()) and int(difficulty) in difficulty_levels:
        difficulty = int(difficulty)
    else:
        print("Invalid difficulty level !!!")
        return False

    # print(f"Difficulty level is {difficulty}")
    if get_game_number == 1:
        from memory_game import play
        result = play(difficulty)
        if result == True:
            add_score(difficulty)
        return result
    elif get_game_number == 2:
        from guess_game import play
        result = play(difficulty)
        if result == True:
            add_score(difficulty)
        return result
    elif get_game_number == 3:
        from currency_roulette_game import play
        result = play(difficulty)
        if result == True:
            add_score(difficulty)
        return result
    else:
        print("Didn't reach Difficulty level is")



# start_play()