from flask import Flask, render_template
from flask_socketio import SocketIO
import logging

import os.path

# Initialize Logger
logger = logging.getLogger(__name__)

# Initialize Flask/SocketIO server
app = Flask(__name__)
socketio = SocketIO(app)

LOG_FILE_NAME="tower-server.log"




if __name__ == '__main__':
    
    # If file not found then create new log file
    if not (os.path.isfile(LOG_FILE_NAME)):
        f = open(LOG_FILE_NAME, "w")
        f.close()
    logging.basicConfig(filename=LOG_FILE_NAME, level=logging.INFO)
    logger.info("Walkie-Talkie tower server is starting") 
    socketio.run(app)

    



@app.route('/health')
def route_health():
    logger.info("Health endpoint was hit")
    logging.info("REEEEEEE")
    return "We gucci"


@socketio.on('connect')
def on_connect(auth):
    logger.info("User Connected")


















