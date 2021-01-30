from flask import Flask, render_template, request
from flask_socketio import SocketIO
import random
from datetime import date
from player import *
from levels import Levels, Solos


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
sio = SocketIO(app)
sio.init_app(app, cors_allowed_origins="*")
# cmd alt l to format
# pip freeze > requirements.txt
# sio = socketio.AsyncServer(cors_allowed_origins='*', ping_timeout=35)


players = Players()
topSolos = TopThree()
# key: sid, value: player
sidDict = dict()
info = {"level": 0, "total": len(Levels)}


@app.route("/")
def index():
    nums = random.sample(Solos, 5)
    levels = []
    for i in nums:
        levels.append(Levels[i-1])
    return render_template("index.html", levels=Levels, solos=levels)


@app.route("/hideabern")
def hide():
    return render_template("hide.html")


@sio.on('connect')
def connected():
    sio.emit('update_solos', topSolos.toTable())
    print('Connected to index', request.namespace, request.sid)


@sio.on('join_game')
def join_game(name):
    print('Joined game', request.sid, name)
    new = Player(name, request.sid)
    players.insertPlayer(new)
    sidDict[request.sid] = new

    sio.emit('your_score', new.to_html(), room=request.sid)
    sio.emit('leaderboard', players.toTable())
    sio.emit('current_round', info["level"])

    print(sidDict)


@sio.on('won_round')
def won_round(name):
    print(name, "won round")
    sid = request.sid
    if sid not in sidDict:
        print("failed win", sid)
    winner = sidDict[sid]
    players.reSort(winner)

    level = (info["level"] + 1) % info["total"]
    info["level"] = level

    sio.emit('your_score', winner.to_html(), room=sid)
    sio.emit('leaderboard', players.toTable())
    sio.emit('current_round', level)


@sio.on('finish_solo')
def finish_solo(name, time):
    new = Solo(name, date.today().strftime("%m/%d/%y"), time)
    topSolos.insert(new)
    sio.emit('update_solos', topSolos.toTable())


@sio.on('disconnect')
def disconnect():
    sid = request.sid
    if sid in sidDict:
        p = sidDict[sid]
        del sidDict[sid]
        players.removePlayer(p)

    print('Disconnected', request.sid)
    sio.emit('leaderboard', players.toTable())


if __name__ == "__main__":
    sio.run(app)
    # sio.run(app, debug=True, host='findthebern.herokuapp.com', port=5004)

