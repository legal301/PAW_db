from flask import Flask, request
import os
from git import Git

exit()
app = Flask(__name__)


@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        DIR = os.getcwd()
        res = Git(DIR).pull()
        return 'Updated PythonAnywhere successfully: '+str(res), 200
    else:
        return 'Wrong event type', 400