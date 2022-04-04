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

# The below function is responsible for the firing of the nerf gun turret
def turret_controller(ROI_list, center):
    # If there is at least face in the ROI_list...
    if len(ROI_list):
        # The list is sorted based on the ROI's distance from the center of the frame.
        ROI_list.sort()
        
        # The ROI closest to center is the first item of the list. This is known as the current ROI
        curr_ROI_obj = ROI_list[0]
        dist_from_center = curr_ROI_obj.dist_from_center
        
        # If the current ROI is 0, then the face is aligned with the center of the frame 
        if not dist_from_center:
            print("Pull trigger")
            # gc.pull_trigger()
        else:
            print("Release trigger")
            # gc.release_trigger()
            if center < curr_ROI_obj.startX:
                print("Move left")
                # gc.move_left()
            else:
                print("Move right")
                # gc.move_right()
    else:
        print("Release trigger")
        # gc.release_trigger()