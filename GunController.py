import pyfirmata
from tkinter import *
import time
import keyboard

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

def main():
    
    
    is_firing = False
    angle = 90
    angle_changed = False
    pin10.write(angle)
    move_servo(0)

    while True:
        if(keyboard.is_pressed("f") and not is_firing):
            print("f reconized")
            is_firing = True
            pull_trigger()
        elif keyboard.is_pressed("r") and is_firing:
            print("r reconized")
            is_firing = False
            release_trigger()
        if keyboard.is_pressed("left"):
            angle -= 1
            angle_changed = True
        elif keyboard.is_pressed("right"):
            angle += 1
            angle_changed = True
        if angle_changed:
            pin10.write(angle)
            angle_changed = False
            time.sleep(0.05)


main()


