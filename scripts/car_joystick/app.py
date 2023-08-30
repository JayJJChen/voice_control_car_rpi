from flask import Flask, render_template

from modules.car import Car

app = Flask(__name__)

car = Car()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/forward', methods=['POST'])
def forward():
    car.forward()
    return 'Forward', 200

@app.route('/backward', methods=['POST'])
def backward():
    car.backward()
    return 'Backward', 200

@app.route('/left', methods=['POST'])
def left():
    car.left()
    return 'Left', 200

@app.route('/right', methods=['POST'])
def right():
    car.right()
    return 'Right', 200

@app.route('/stop', methods=['POST'])
def stop():
    car.stop()
    return 'Stop', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
