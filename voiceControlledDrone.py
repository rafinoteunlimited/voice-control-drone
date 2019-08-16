from flask import Flask
import sys
import os

app = Flask(__name__)

@app.route('/launch')

def takeoff ():
    os.system('python3 drone.py takeoff')
    return "drone hopefully taking off"

@app.route("/land")
def land ():
    os.system('python3 drone.py land')
    return "drone hopefully landing"

@app.route("/forward")
def forward ():
    os.system('python3 drone.py forward')
    return "drone moving forward"

@app.route("/back")
def back ():
    os.system('python3 drone.py back')
    return "drone moving back"

@app.route("/right")
def right ():
    os.system('python3 drone.py right')
    return "drone moving right"

@app.route("/left")
def left ():
    os.system('python3 drone.py left')

@app.route("/up")
def up ():
    os.system('python3 drone.py up')
    return "drone moving up"

@app.route("/down")
def down ():
    os.system('python3 drone.py down')
    return "drone moving down"

@app.route("/flip")
def frontflip ():
    os.system('python3 drone.py flip')
    return "drone doing a frontflip"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
