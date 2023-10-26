

from app import start_play, welcome


welcome()
result = start_play()
while True:
    # result = start_play()
    # print(result)
    if result == True:
        print("WELL DONE ! ! ! ! !")
        # try_again = input("Would you like to try again: Y | N ")
        # if try_again in ['Y', 'y', 'Yes', 'yes']:
        #     result = start_play()
        # else:
        #     print("See you soon")
    elif result == False:
        print("Game Failed")
        # try_again = input("Would you like to try again: Y | N ")
        # if try_again in ['Y', 'y', 'Yes', 'yes']:
        #     result = start_play()
        # else:
        #     print("See you soon")
        #     break
    else:
        print("Something went wrong - please try again")
        # break

    try_again = input("Would you like to try again: Y | N ")
    if try_again in ['Y', 'y', 'Yes', 'yes']:
        result = start_play()
    else:
        print("See you soon")
        break

