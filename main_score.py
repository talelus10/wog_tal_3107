
from flask import Flask

import utils


app = Flask(__name__)

@app.route("/")
def score_server():
    my_file = open(utils.SCORES_FILE_NAME)
    number_of_lines = 0
    for score1 in my_file.readlines():
        SCORE = score1
        number_of_lines = number_of_lines + 1
    my_file.close()
    if number_of_lines == 1:

        html_success_message = '''
                <html>
                    <head>
                        <title>Score Game</title>
                    </head>
                    <body>
                        <h1>The Score Is: </h1>
                        <div id="score">{SCORE}</div>
                    </body>
                </html>'''.format(SCORE=SCORE)
        # return '<p>Hello, World!</p>'
        return html_success_message
    else:
        ERROR = "Something wrong in Scores file"
        html_error_message = '''
                <html>
                    <head>
                        <title>Score Game</title>
                    </head>
                    <body>
                        <h1>ERROR: </h1>
                        <div id="score" style="color:red">{ERROR}</div>
                    </body>
                </html>'''.format(ERROR=ERROR)
        # return '<p>Hello, World!</p>'
        return html_error_message

app.run('0.0.0.0')

score_server()