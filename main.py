from flask import Flask, render_template, request
from flask_socketio import SocketIO
from player import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
sio = SocketIO(app)
sio.init_app(app, cors_allowed_origins="*")
# cmd alt l to format
# pip freeze > requirements.txt
# sio = socketio.AsyncServer(cors_allowed_origins='*', ping_timeout=35)


players = Players()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/find")
def find():
    return render_template("find.html")


@sio.on('connect')
def connected():
    print('Connected to index', request.namespace, request.sid)


@sio.on('join_game')
def join_game(name):
    print('Joined game', request.namespace, request.sid, name)


@sio.on('disconnect')
def disconnect():
    print('Disconnected')


if __name__ == "__main__":
    sio.run(app)
