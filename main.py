from flask import Flask, request
import os
from git import Git


app = Flask(__name__)


@app.route('/u', methods=['GET'])
def webhook():
    DIR = os.getcwd()
    res = Git(DIR).pull()
    return 'Updated PythonAnywhere successfully: '+str(res), 200


if __name__ == "__main__":
    app.run()