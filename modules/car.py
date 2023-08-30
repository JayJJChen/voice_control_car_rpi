import RPi.GPIO as GPIO
from modules.config import WHEEL_PINS

# Uncomment the above import when running on a Raspberry Pi

class Wheel:
    def __init__(self, in1, in2):
        self.in1 = in1
        self.in2 = in2
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
    
    def forward(self):
        GPIO.output(self.in1, True)
        GPIO.output(self.in2, False)
    
    def backward(self):
        GPIO.output(self.in1, False)
        GPIO.output(self.in2, True)
    
    def stop(self):
        GPIO.output(self.in1, False)
        GPIO.output(self.in2, False)

class Car:
    def __init__(self):
        # GPIO.setmode(GPIO.BOARD)
        GPIO.setmode(GPIO.BCM)
        self.front_left = Wheel(WHEEL_PINS['FRONT_LEFT'][0], WHEEL_PINS['FRONT_LEFT'][1])
        self.front_right = Wheel(WHEEL_PINS['FRONT_RIGHT'][0], WHEEL_PINS['FRONT_RIGHT'][1])
        self.back_left = Wheel(WHEEL_PINS['BACK_LEFT'][0], WHEEL_PINS['BACK_LEFT'][1])
        self.back_right = Wheel(WHEEL_PINS['BACK_RIGHT'][0], WHEEL_PINS['BACK_RIGHT'][1])
    
    def forward(self):
        self.front_left.forward()
        self.front_right.forward()
        self.back_left.forward()
        self.back_right.forward()
        
    def backward(self):
        self.front_left.backward()
        self.front_right.backward()
        self.back_left.backward()
        self.back_right.backward()
    
    def left(self):
        self.front_left.backward()
        self.front_right.forward()
        self.back_left.backward()
        self.back_right.forward()
    
    def right(self):
        self.front_left.forward()
        self.front_right.backward()
        self.back_left.forward()
        self.back_right.backward()
    
    def stop(self):
        self.front_left.stop()
        self.front_right.stop()
        self.back_left.stop()
        self.back_right.stop()
