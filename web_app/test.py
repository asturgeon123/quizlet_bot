import sys
import os
from time import sleep

from flask import Flask, send_from_directory, request,jsonify,render_template
from flask_cors import CORS

#Server Side Requests
from flask_socketio import SocketIO, emit
#from src import keyboard_manger
import pyperclip
from random import random
from threading import Thread, Event




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

def autosearch():
    last_data = None
    while not thread_stop_event.isSet():
        # get clipboard data
        data = pyperclip.paste()
        if data != last_data:
            last_data = data
            socketio.emit('newquery', {'query': last_data}, namespace='/test')


def randomNumberGenerator():
    """
    Generate a random number every 1 second and emit to a socketio instance (broadcast)
    Ideally to be run in a separate thread?
    """
    #infinite loop of magical random numbers
    print("Making random numbers")
    while not thread_stop_event.isSet():
        number = round(random()*10, 3)
        print(number)
        socketio.emit('newquery', {'query': number}, namespace='/test')
        socketio.sleep(5)


#SocketIO Stuff
thread = Thread()
thread_stop_event = Event()

@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread
    print('Client connected')

    #Start the autosearch thread only if the thread has not been started before.
    if not thread.is_alive():
        print("Starting Thread")
        thread = socketio.start_background_task(autosearch)

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')





if __name__ == '__main__':
    #p = Process(target=autosearch)
    #p.start()
    socketio.run(app)
    #app.run(threaded=True)


    


