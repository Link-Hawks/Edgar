
from flask import Flask
from livereload import Server, shell
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

from routes.edgar import *

if __name__ == '__main__':
    app.debug = True
    socketio.run(app,host='0.0.0.0')