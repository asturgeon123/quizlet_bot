import sys
import os
from time import sleep

from flask import Flask, send_from_directory, request,jsonify,render_template
from flask_cors import CORS

#Server Side Requests
from flask_socketio import SocketIO, emit
#from src import keyboard_manger
import pyperclip

import webbrowser
from multiprocessing import Process

import parse

from src.answer_scrapper import answer




#to build -- cd into directory and run "yarn run make"


app = Flask(__name__)
socketio = SocketIO(app,cors_allowed_origins="*")
#CORS(app)


@socketio.on('connect')
def test_connect(auth):
    emit('my response', {'data': 'Connected'})


@socketio.on('connect')
def auto_search():
    emit('after connect',  {'data':'AutoSearch Starting...'})

    #socketio.emit('message',  {'data':'YOOOOOOOOOOO'},namespace='/autosearch')

    last_data = None
    while True:
        sleep(0.2)
        # get clipboard data
        data = pyperclip.paste()
        if last_data != data:
            print("---- [!] ---- NEW DATA",data,flush=True)
            last_data = data
            #with app.test_request_context('/'):
            print("EMITTINGGGGGGG",flush=True)
            #emit('message',  {'data':data})
            socketio.emit('message',  {'data':data},namespace='/autosearch')


    

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


def open_browser():
    sleep(2)
    webbrowser.open('http:/127.0.0.1:5000')
    sys.exit()

def autosearch1():
    last_data = None
    while True:
        # get clipboard data
        data = pyperclip.paste()
        if data != last_data:
            print("---- [!] ---- NEW DATA",data,flush=True)
            last_data = data
            #with app.test_request_context('/'):
            print("EMITTINGGGGGGG",flush=True)
            socketio.emit('message',  {'data':data},namespace='/autosearch')




if __name__ == '__main__':
    #p = Process(target=autosearch)
    #p.start()
    socketio.run(app)
    #app.run(threaded=True)


    


