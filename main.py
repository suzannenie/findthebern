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
# key: sid, value: player
sidDict = dict()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hideabern")
def hide():
    return render_template("find.html")


@sio.on('connect')
def connected():
    print('Connected to index', request.namespace, request.sid)


@sio.on('join_game')
def join_game(name):
    print('Joined game', request.sid, name)
    new = Player(name, request.sid)
    players.insertPlayer(new)
    sidDict[request.sid] = new

    you = "<p>You (" + name + ") have " + str(new.points) + " points</p><br>"
    sio.emit('leaderboard', you+players.toTable())

    print(sidDict)


@sio.on('disconnect')
def disconnect():
    sid = request.sid
    if sid in sidDict:
        p = sidDict[sid]
        del sidDict[sid]
        players.removePlayer(p)

    print('Disconnected', request.sid)
    print(sidDict)


if __name__ == "__main__":
    sio.run(app)
