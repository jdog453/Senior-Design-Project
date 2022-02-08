
# User Documentation and User Manual

The device has not been completely designed yet. However, we have an idea of how the user will interact with the device once it is complete. Our below instructions/FAQ will detail the user’s interaction with the device based on the current idea of how the device will be designed.

  
## Table of Contents
- Abstract directions

	- Set up the device

	- Turn on the raspberry pi

	- Train the facial recognition model to recognize specific faces

	- Register/Login to the webapp

- FAQs  3

	- Why is the nerf gun turret not turning on?

	- Why is the nerf gun turret on but not firing?

	- Why is the nerf gun turret firing at someone that is marked as safe?

	- Why does the nerf gun turret not fire at people who are not marked as safe?

	- Why is the nerf gun turret not aiming? Alternatively, when the nerf gun turret aims, why does it aim slowly?

  
  

-   # Abstract directions:
    

-   ## Set up the device.
    

-   Place the stand in an area with a large amount of space in front of the device.
    

	-   Ensure that there is a wall outlet near where the device is placed. This will be necessary for the raspberry pi to be powered.
    
	-   The front of the device is the side whose nerf gun turret barrel is facing.
    
	-   Make sure that the nerf gun turret is loaded with nerf gun turret ammunition.
    
	-   Make sure that the nerf gun turret is powered on. I.e., ensure that the device has batteries.
    

-   ## Turn on the raspberry pi device.
    

	-   Note: The current plan is to use the raspberry pi. However, facial recognition on such a device is computationally expensive and would reduce the camera’s performance to less than ~3 frames per second. This is too little for our purposes. We are currently researching how to improve this. The easiest solution is to use a laptop to accomplish this. Regardless, the remainder of the directions will be in regard to the raspberry pi.
    
	-   Plug the raspberry pi power supply into a wall outlet. Plug the power supply into the raspberry pi device.
    
	-   From there, once the pi is powered on, a script on the system will begin the program that is responsible for facial detection/recognition. The user will not need to perform any additional steps to begin this program as it starts on the boot of the device.
    

-   ## Train the facial recognition model to recognize specific faces.
    

-   The facial recognition model needs to be trained with the faces that you wish to be marked as “safe”. This training is done by providing the model with pictures of these faces. The more pictures, the more accurate the model. The model needs to be retrained every time a new face is added/removed from the list of safe faces.
    
-   The pictures should be of one’s face as the face is directly facing the camera.
    
-   There should be at least 6 pictures and at most 1000 pictures of the same face.
    
-   As of right now, with our current design (although this will likely be improved as time passes), the user must manually insert a directory representing a face into a directory.
    

	-   The face directory will contain subdirectories. Subdirectory titles will be of the name of the face that is contained within the subdirectory.
    

		-   E.g. should the user wish to train the model with pictures of a face belonging to an individual named “Ben,” then the directory structure will be:
    

			-   Faces > Ben > ben_image_1, ben_image_2, …
    

	-   The file format of each image can be either png or jpeg
    

-   Assuming that the raspberry pi will still be used for facial recognition (and not replaced with another device), the training must be done on a more powerful machine that is not the raspberry pi (the pi is too weak to efficiently perform the training).
    
-   Once the faces directory has been updated, the facial training python file must be rerun. This can be done from the command line. If the training file is titled, “faces_train.py” and the user has python3 installed, the following command will run the file and create a new model:
    

	-   python3 faces_train.py
    

-   This will generate a “yml” file. This file needs to be exported to the pi. Specific instructions on how this can be will be updated later; however, for now, a file transferring app, such as WinSCP, can be used.
    
-   Once exported, the .yml file must replace the current yml file in the correct directory (the name of this directory will be updated as more of the project is developed).
    
-   Once this occurs, then the user can use the nerf gun turret as normal.
    

-   ## Register/Login to the webapp.
    

-   When opening the webapp, there will be a login page. If you have an account, log in. If you do not, click the “Register” button.
    

	-   This will take you to a registration page. Enter your information and click “Create Account”.
    

-   In the webapp, click the “Activate” button to activate the turret.
    
-   You will also be able to see a live feed from the camera.
    

  

-   # FAQs
    

-   ## Why is the nerf gun turret not turning on?
    

	-   Make sure that the gun has batteries and that the batteries are not dead.
    

-   ## Why is the nerf gun turret on but not firing?
    

	-   Make sure that the gun is loaded.
    
	-   It is also possible that the gun is jammed. In this case, open the sliding hatch on top of the gun and manually remove the jammed dart.
    

-   ## Why is the nerf gun turret firing at someone that is marked as safe?
    

	-   Try to add the person’s face to the model again and retrain it.
    

-   ## Why does the nerf gun turret not fire at people who are not marked as safe?
    

	-   Make sure the camera’s lens is clean, and that the gun’s batteries are not dead.
    

-   ## Why is the nerf gun turret not aiming? Alternatively, when the nerf gun turret aims, why does it aim slowly?
    

	-   Make sure that the servo motor battery packs are not dead.

