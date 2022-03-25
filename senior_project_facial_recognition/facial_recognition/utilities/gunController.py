import pyfirmata
from tkinter import *
import time

global is_firing
global angle
global pin9
global pin10
global iter8

class gunController:
    def __init__(self):
        self.board=pyfirmata.Arduino('COM3')

        self.pin9 = self.board.get_pin('d:9:s')
        self.pin10 = self.board.get_pin('d:10:s')

        self.iter8 = pyfirmata.util.Iterator(self.board)
        self.iter8.start()
        
        self.is_firing = False
        self.angle = 80
        self.pin10.write(self.angle)

    def move_servo(self, angle):
        self.pin9.write(angle)

    def pull_trigger(self):
        if not self.is_firing:
            self.move_servo(180)
            self.is_firing = True

    def release_trigger(self):
        if self.is_firing:
            self.move_servo(0)
            self.is_firing = False

    def move_left(self):
        if(self.angle > 60):
            self.angle -= 1
            self.pin10.write(self.angle)
            time.sleep(0.05)

    def move_right(self):
        if(self.angle < 95):
            self.angle += 1
            self.pin10.write(self.angle)
            time.sleep(0.05)
            