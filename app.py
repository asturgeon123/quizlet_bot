import sys
import os
from time import sleep

from flask import Flask, send_from_directory, request,jsonify,render_template
from flask_cors import CORS

import webbrowser
from multiprocessing import Process

import parse



#SRC isnt importing in compiled version -- PROBLEM
try:
    from src.answer_scrapper import find_answer
except ModuleNotFoundError:
    scriptdir, script = os.path.split(os.path.abspath(__file__))
    print(scriptdir)

    #Import the SRC file from parent dir
    path = scriptdir + r'\src'
    sys.path.insert(0,path)
    print(path)
    from src.answer_scrapper import find_answer

    


app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    #return send_from_directory('', 'index.html')
    return render_template('index.html')


@app.route('/question', methods=['GET', 'POST'])
def question():
    data = request.form['question']  # pass the form field name as key
    answer = find_answer(data)
    #print(data)

    return jsonify(answer[1]), 200

def open_browser():
    sleep(2)
    webbrowser.open('http:/127.0.0.1:5000')
    sys.exit()


'''
def main(): #Entry Point Function
    if __name__ == '__main__':
        p = Process(target=open_browser)
        p.start()
        app.run()
'''


if __name__ == '__main__':
    #p = Process(target=open_browser)
    #p.start()
    app.run()


    


