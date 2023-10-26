
import utils

def add_score(difficulty):
    my_file = open(utils.SCORES_FILE_NAME)
    number_of_lines=0

    for score in my_file.readlines():
        # print(score, end="")
        # print(type(score))
        # score = int(score)
        # print(type(score))
        number_of_lines = number_of_lines + 1

    my_file.close()
    if number_of_lines == 1 and score.isdigit():
        points_of_winning = int(score)+(difficulty*3)+5
        my_file = open(utils.SCORES_FILE_NAME, "w")
        my_file.write(str(points_of_winning))
        my_file.close()
    else:
        my_file = open(utils.SCORES_FILE_NAME, "r+")
        my_file.truncate(0)
        my_file.close()



# add_score(4)