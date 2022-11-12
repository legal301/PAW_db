from flask import Flask, request, jsonify
import os
from git import Git


app = Flask(__name__)


@app.route('/u', methods=['GET'])
def webhook():
    DIR = os.getcwd()
    res = Git(DIR).pull()
    return 'Updated PythonAnywhere successfullyy: '+str(res), 200

@app.route("/size")
def size():
    s = str(os.system("du -s /home")).split()
    return jsonify({"size": s})


if __name__ == "__main__":
    app.run()
