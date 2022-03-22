import pyfirmata
from tkinter import *
import time

global is_firing
global angle
global pin9
global pin10
global iter8

def start_up():
    board=pyfirmata.Arduino('COM5')

    pin9 = board.get_pin('d:9:s')
    pin10 = board.get_pin('d:10:s')

    iter8 = pyfirmata.util.Iterator(board)
    iter8.start()

def move_servo(angle):
    pin9.write(angle)

def pull_trigger():
    if not is_firing:
        move_servo(180)
        is_firing = True

def release_trigger():
    if is_firing:
        move_servo(0)
        is_firing = False
    
def move_left():
    if(angle > 0):
        angle -= 1
        pin10.write(angle)
        time.sleep(0.05)
    
def move_right():
    if(angle < 256):
        angle += 1
        pin10.write(angle)
        time.sleep(0.05)


