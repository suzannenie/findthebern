from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
sio = SocketIO(app)
sio.init_app(app, cors_allowed_origins="*")
# cmd alt l to format
# pip freeze > requirements.txt
# sio = socketio.AsyncServer(cors_allowed_origins='*', ping_timeout=35)


@app.route("/")
def index():
    return render_template("index.html")


@sio.on('connect')
def connected():
    print('Connected')


@sio.on('disconnect')
async def disconnect():
    print('Disconnected')


if __name__ == "__main__":
    sio.run(app, debug=True)
