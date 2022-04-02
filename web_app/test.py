import sys
import os
from time import sleep

from flask import Flask, send_from_directory, request,jsonify,render_template
from flask_cors import CORS

#Server Side Requests
#from src import keyboard_manger
import pyperclip



import webbrowser
from multiprocessing import Process

import parse

from src.answer_scrapper import answer




#to build -- cd into directory and run "yarn run make"


app = Flask(__name__)
CORS(app)





@app.route("/")
def index():
    #return send_from_directory('', 'index.html')
    return render_template('index.html')


@app.route('/question', methods=['GET', 'POST'])
def question():
    question = request.form['question']  # pass the form field name as key
    return_data = answer(question).find()
    #print(data)

    return jsonify(return_data), 200


@app.route('/clipboard', methods=['GET'])
def clipboard():
    data = {'data':pyperclip.paste()}  # get clipboard data
    #print(data)

    return jsonify(data), 200


def open_browser():
    sleep(2)
    webbrowser.open('http:/127.0.0.1:5000')
    sys.exit()





if __name__ == '__main__':
    #p = Process(target=autosearch)
    #p.start()
    app.run(threaded=True)


    


