# **Table Of Contents**

**[Abstract](#Abstract)**

**[Project Description](#project-description)**

**[User Manual](#user-manual)**

**[User Stories](#user-stories)**

**[Design Diagrams](#design-diagrams)**

[Level 0](#level-0)

[Level 1](#level-1)

[Level 2](#level-2)

**[Project Tasks and Timeline](#project-tasks-and-timelines)**

[Task List](#task-list)

[Timeline](#timeline)

[Effort Matrix](#effort-matrix)

**[PPT Slideshow](#ppt-slideshow)**

[Final Results](#final-results)

[Summary of Hours](#summary-of-hours)

**[Self-Assessment Essays](#self-assessment-essays)**

[Andrew Dygert - Fall](#andrew-dygert---fall)

[Andrew Dygert - Spring](#andrew-dygert---spring)

[Austen Brownfield - Fall](#austen-brownfield---fall)

[Austen Brownfield - Spring](#austen-brownfield---spring)

[Fred Jenks - Fall](#fred-jenks---fall)

[Fred Jenks - Spring](#fred-jenks---spring)

[Jared Musser - Fall](#jared-musser---fall)

[Jared Musser - Spring](#jared-musser---spring)

**[Professional Biographies](#professional-biographies)**

[Andrew Dygert](#andrew-dygert)

[Austen Brownfield](#austen-brownfield)

[Fred Jenks](#fred-jenks)

[Jared Musser](#jared-musser)

**[Poster](#poster)**

**[Budget](#budget)**

**[Appendix](#appendix)**

# Abstract

Personal security is a major issue during these times. Individuals shouldn&#39;t need to worry about the safety of their personal belongings while he or she isn&#39;t there to ensure their safety. Our team has decided to pursue the research and development of a project that seeks to remedy this issue: an automated nerf gun that fires at trespassers. No longer will people be worried about the safety of their belongings when this device is in use. While this device is on and in a room, should a trespasser be detected, the nerf gun will fire at them. The sudden confusion and fear of being shot at by a nerf gun will scare away any unwanted guests.

# Project Description

While most people lock the doors in and out of their house, how many individuals lock doors within their house while they&#39;re away? Should an intruder get past the first line of defense, then an individual&#39;s belongings are at risk of being stolen unless there are additional countermeasures. Individuals could purchase costly security measures, but where&#39;s the fun in that? An automated nerf gun turret is an inexpensive, secure, and fun option for individuals to consider.

Several Python libraries (OpenCV, dlib, face_recogntion, Jupyter notebook) were leveraged to implement facial detection and recognition. This solution allows users to train his/her own facial recognition model via a laptop. A wooden box was built to hold the nerf gun. This container is attached to a tripod and can be placed at any location if there are nearby outlets to power an arduino and a stand to hold the laptop. Both the arduino and webcam are connected to the laptop via USB. The webcam is placed at the tip of the nerf gun. A servo motor is connected to the container and rotates based on the position of one's face on the webcam. A lazy susan facet is used to allow easy rotation. If an unknown individual is detected and they are positioned in the center of the webcam, then the nerf gun will fire. Our design allows the nerf gun to rotate ~180 degrees while tracking unknown faces. The magazine holds eighteen nerf darts, and the user must manually reload once it's empty.

Different variations of our facial detection and recognition are available for use. The user can choose to use only facial detection where every detected face will be shot at. Several facial recogntion models are provided ranging from poor accuracy and great video performance to great accuracy and poor video performance. The latter can only be used if the user's laptop has a CUDA compatible GPU. Instructions for running each variation are provided in the User Manual.

# UI Specifications

The only user interface aspects of our project are the Jupyter notebooks and video stream. The notebook directories are organized in a way that we believe allows the user to best understand the locations of the necessary files. When the facial detection and recognition notebooks are running, the user is able to view the stream on his/her laptop. On the stream, recognized faces will be marked with a rectangle and a label showing either the recognized face's name or "unknown."

# Test plan and results

Test Case Descriptions

FD1.1  Facial Detection Test 1
FD1.2  The purpose of this test is to ensure that the facial detection program detects when a face
	is on the camera.
FD1.3	We will test this by having individuals with visible faces appear on the camera at various 
	distances and positions from the camera. We will know if a face is detected by observing 
	the output of the program ??? if a square is drawn around a face, then the face has been
	detected.

FD2.1  Facial Detection Test 2
FD2.2  The purpose of this test is to ensure that the facial detection program detects a face when
	the face is of a darker complexion
FD2.3	We will test this by having individuals with visible faces of a darker complexion appear
on the camera at various distances and positions from the camera. We will know if a face
is detected by observing the output of the program ??? if a square is drawn around a face,
then the face has been	detected.

FR1.1  Facial Recognition Test 1
FR1.2  The purpose of this test is to ensure that the facial recognition program recognizes any 
	faces that were added as ???safe??? faces.
FR1.3	We will test this by having individuals with visible faces who are on the ???safe??? face list
appear on the camera at various distances and positions from the camera. We will know if
a face is recognized by observing the output of the program ??? if a square is drawn around
a face and the face has been correctly labeled with the name of who that face belongs to,
then the face has been correctly recognized.

T1.1  	Turret Test 1
T1.2 	The purpose of the test is to make sure the turret can hit a target to the far left of the screen
T1.3	We will have a target enter at the far left on the screen, and see if the turret is able to rotate properly in order to hit the target

T2.1  	Turret Test 2
T2.2 	The purpose of the test is to make sure the turret can hit a target to the far right of the screen
T2.3	We will have a target enter at the far right on the screen, and see if the turret is able to rotate properly in order to hit the target

T3.1  	Turret Test 3
T3.2 	The purpose of the test is to make sure the turret can fire in an adequate time
T3.3	We will have a target appear on the screen, and measure the time it takes to fire from the time the person enters the screen

| Test Case | Result |
| --- | --- |
| FD1 | Passed |
| FD2 | Passed |
| FR1 | Passed |
| T1 | Passed |
| T2 | Passed |
| T3 | Passed |

additionally, there were test cases that were removed due to the functionality being unable to be completed because of time constraints

# User Manual

* Directions:
    * Set up the device.
        * Place the stand in an area with a large amount of space in front of the device.
            * Ensure that there is a wall outlet near where the device is placed. This will be necessary for the devices to be powered.
            * The front of the device is the side whose nerf gun turret barrel is facing.
            * Make sure that the nerf gun turret is loaded with nerf gun turret ammunition.
            * Make sure that the nerf gun turret is powered on. I.e., ensure that the device has batteries.
    * Download the source code
        * The code is available on github at the following link: [https://github.com/jdog453/Senior-Design-Project](https://github.com/jdog453/Senior-Design-Project)
    * Set up the environment needed to run the code:
        * There are several versions of this software that can be used:
            * Senior-Design-Project > senior_project_facial_recognition > ???
                * facial_detection
                    * This is only facial detection. There is no recognition. This means that there is no training on ???safe??? faces and that the nerf gun turret will blast at anyone indiscriminately
                * facial_recognition
                    * This uses facial recognition but with a less-than-ideal model (i.e., the accuracy of the model is not the best).
                    * However, this should be used if:
                        * The user does not have a CUDA compatible GPU
                    * Although much less accurate than the below version, this can be used without GPU support.
                * facial_recognition_V2
                    * There are two versions of this software that can be used. Both are found within the same file. The user simply changes the ???detection_method??? input parameter to be:
                        * hog
                            * Less accurate than cnn, but quicker to encode the faces and better fps of the video stream
                        * cnn
                            * More accurate than hog, but takes longer to encode the faces and slightly worse fps in video stream
                    * If the user???s GPU is CUDA compatible and the GPU is ???good??? then this method should be used.
        * What???s needed for all versions:
            * Python
                * The 64-bit version was used for this project.
                    * The 32-bit version was never tested. However, the assumption is that downloading the 32-bit libraries for the other packages should allow this to work.
                    * Instructions will continue by outlining the libraries used with the 64-bit version of Python
            * Windows OS
                * This was not tested on another OS. As such, the instructions will only be for this OS.
            * Opencv-python 4.3.0.38
            * Face-recognition library
            * Imutils library
        * The instructions below are for the ???V2??? version of facial recognition.
            * The steps to set this up are very involved, time-consuming, and needlessly obtuse. However, I???ve tried to compile all of the resources I used to set this up on my machine to make things easier:
                * Install Visual Studio (2019)
                    * Other versions will likely work as well.
                    * In the ???Visual Studio Installer??? application:
                        * Select ???modify???
                        * Along the right panel, drop the ???Desktop Development with C++??? menu
                        * Among the already-selected items (if any), ensure that the following are selected:
                            * Windows 10 SDK
                            * C++ CMake tools for Windows
                            * MSVC build tools
                        * Select ???modify???
                * Install CMake
                * Install Anaconda
                * Install NVIDIA CUDA Toolkit and cuDNN:
                    * Instructions to set this up can be found on the site:
                        * [https://medium.com/analytics-vidhya/cuda-toolkit-on-windows-10-20244437e036](https://medium.com/analytics-vidhya/cuda-toolkit-on-windows-10-20244437e036)
                    * Additional instructions to help with the process:
                        * [https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html)
                        * [https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html) 
                * Install dlib using conda with CUDA enabled:
                    * Follow the below instructions **up to but not including the ???nvcc??? part:**
                        * [https://gist.github.com/nguyenhoan1988/ed92d58054b985a1b45a521fcf8fa781](https://gist.github.com/nguyenhoan1988/ed92d58054b985a1b45a521fcf8fa781)
                    * Perform the following steps while in your conda environment:

                            $ git clone https://github.com/davisking/dlib.git


                            $ cd dlib


                            $ mkdir build


                            $ cd build


                            $ cmake .. -DDLIB_USE_CUDA=1 -DUSE_AVX_INSTRUCTIONS=1


                            $ cmake --build .


                            $ cd ..


                            $ python setup.py install --no DLIB_GIF_SUPPORT

                        * References for above steps:
                            * [https://pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/](https://pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/)
                            * [https://github.com/davisking/dlib/issues/2358](https://github.com/davisking/dlib/issues/2358)
                * Troubleshooting:
                    * Unable to open conda environment:
                        * If there is a space character in your anaconda path, refer to the below steps:
                            * Edit the "C:\ProgramData\Anaconda3\Scripts\activate.bat" file and add the following before the first ???@if???:

                                @set TEMP=C:/temp


                                @set TMP=C:/temp

                            * Reference:
                                * [https://stackoverflow.com/questions/60789886/error-failed-to-create-temp-directory-c-users-user-appdata-local-temp-conda](https://stackoverflow.com/questions/60789886/error-failed-to-create-temp-directory-c-users-user-appdata-local-temp-conda)
                    * Unable to download CUDA toolkit from reference site
                        * Sometimes the site is down and does not allow downloads. The user will need to check the site occasionally to see if the download is available.
    * Begin running the turret with only facial detection
        * Navigate to Senior-Design-Project/senior_project_facial_recognition/facial_detection/notebooks/detect_faces_stream.ipynb and run the code.
            * The parameters do not need adjusted
        * The stream should begin and the turret is on.
        * To power off the turret, click the ???q??? key while the stream is up. This will close the stream and end the program.
    * Train the facial recognition model to recognize specific faces.
        * The facial recognition model needs to be trained with the faces that you wish to be marked as ???safe???. This training is done by providing the model with pictures of these faces. The more pictures, the more accurate the model. The model needs to be retrained every time a new face is added/removed from the list of safe faces.
        * The pictures should be of one???s face as the face is directly facing the camera.
        * There should be at least 6 pictures and at most 100 pictures of the same person???s face.
        * The user must manually insert a directory representing a face.
            * Navigate to ???Senior-Design-Project/senior_project_facial_recognition/facial_recognition_data/faces_dataset???
            * Create a directory with the name of the person who wishes to be marked as safe.
                * E.g. should the user wish to train the model with pictures of a face belonging to an individual named ???Ben,??? then the directory will be called ???ben???
            * Within this directory, insert pictures of this individual???s face.
                * The file format of each image can be either png or jpeg
                * Note: We???ve also included a script that will take a video and read its frames. These frames can be used as images for the directory. See _Collecting Pictures** **_section.
        * Once the directory has been updated, embeddings must be generated for each face. This is a necessary step to train the model to recognize the faces.
        * Senior-Design-Project > senior_project_facial_recognition > facial_recognition:
            * Navigate to ???Senior-Design-Project/senior_project_facial_recognition/facial_recognition/notebooks/extract_embeddings.ipynb??? and run the code.
                * The data parameters do not need to be adjusted for this.
            * Once this step completes, the model must be trained with the data generated from the previous step.
            * Navigate to ???Senior-Design-Project/senior_project_facial_recognition/facial_recognition/notebooks/train_model.ipynb??? and run the code.
                * The data parameters do not need to be adjusted for this.
            * Once trained, the stream can be started.
            * Navigate to ???Senior-Design-Project/senior_project_facial_recognition/facial_recognition/notebooks/recognize_stream.ipynb??? and run the code.
                * It may take some time (~1-2 mins) for the stream to begin.
                * Once the stream begins, a window will open on the user???s machine. This window shows the live feed from the stream.
            * The stream should begin and the turret is on.
            * To power off the turret, click the ???q??? key while the stream is up. This will close the stream and end the program.
        * Senior-Design-Project > senior_project_facial_recognition > facial_recognition_V2
            * Navigate to Senior-Design-Project > senior_project_facial_recognition > facial_recognition_V2 > notebooks > encode_faces.ipynb
                * Adjust the ???detection_method??? data parameter based on which implementation you???d like to use. The other parameters do not need to be adjusted.
            * Once this completes, the stream can be viewed.
            * Navigate to Senior-Design-Project > senior_project_facial_recognition > facial_recognition_V2 > notebooks > recognize_faces_stream.ipynb
                * Adjust the ???detection_method??? data parameter based on which implementation you???d like to use. The other parameters do not need to be adjusted.
            * The stream should begin and the turret is on.
            * To power off the turret, click the ???q??? key while the stream is up. This will close the stream and end the program.
    * Collecting Pictures
        * The process of collecting pictures for an individual can be long and tedious depending on how many pictures one wishes to use. We???ve added a script to help with this process.
        * First, record a video of the individual you wish to train. This video should be of the individual???s face close to the camera with no other items elsewhere that look like faces.
            * The video length does not matter too much. If you wish to collect x pictures from a video that contains &lt; x frames, then an error will occur. The longer the video, the more spread out the pictures from the video that will be used to train the model will be.
        * Navigate to ???Senior-Design-Project/senior_project_facial_recognition/facial_recognition_data/utilities/vid_split.ipynb???
            * Change the ???input_path??? parameter to the input path of the video.
            * Change the ???max_pictures??? parameter to an integer representing the max amount of pictures you???d like to take from the video
            * Change the ???output_dir??? parameter to the directory of where the pictures should be saved.
                * This should be to directory that was created for the individual you???d like to train the model on
            * Change the ???file_pre_name??? parameter to the text that you???d like to be prepended to the file name.
        * Run the code to get pictures.
        * Note: Sometimes the pictures that are gotten from the input video are rotated. If this occurs, the user must manually rotate them back to be the correct angle.
            * This can be done by right-clicking the image > rotate left/right. This can also be done in bulk by selecting multiple images at once.
* FAQs
    * Why is the nerf gun turret not turning on?
        * Make sure that the gun has batteries and that the batteries are not dead.
    * Why is the nerf gun turret on but not firing?
        * Make sure that the gun is loaded.
        * It is also possible that the gun is jammed. In this case, open the sliding hatch on top of the gun and manually remove the jammed dart.
    * Why is the nerf gun turret firing at someone that is marked as safe?
        * Try to add the person???s face to the model again and retrain it.
        * Facial recognition models are never 100% accurate. A good rule of thumb is that the more data there is to recognize a person, the better the model will be.
    * Why does the nerf gun turret not fire at people who are not marked as safe?
        * Make sure the camera???s lens is clean, and that the gun???s batteries are not dead.
    * Why is the nerf gun turret not aiming? Alternatively, when the nerf gun turret aims, why does it aim slowly?
        * Make sure that the servo motor battery packs are not dead.


# User Stories

- As a homeowner, I want this automated nerf gun turret to fire when trespassers enter a protected room, so that the intruder will retreat and that my items will be safe.
- As a user of this device, I want the automated nerf gun turret to fire at the intruder once he/she has been identified via facial recognition or motion detection, so that the intruder will retreat and that my items will be safe.
- As a user of this device, I want to be able to view the video feed of the attached camera to the nerf gun turret, so that I can personally view the room that it&#39;s protecting.
- As a user of this device, I want there to be adjustable legs so that the turret can adjust to different environments.
- As a user of this device, I would like a remote activation feature so that I can make sure that it is always on when I need it to be.

# Design Diagrams

## Level 0

![Level 0 Diagram](https://github.com/jdog453/Senior-Design-Project/blob/26e5da36bfb9869cddf6f5705d973006a3990167/Design%20Diagrams/D0.drawio.png)

The above image represents the lowest level design of our project. The user will activate the machine. If a face is detected, the firing angle is calculated and the nerf gun turret fires.

## Level 1

![Level 1 Diagram](https://github.com/jdog453/Senior-Design-Project/blob/26e5da36bfb9869cddf6f5705d973006a3990167/Design%20Diagrams/D1.drawio.png)

This is our original diagram. The user uses a web app that turns on the camera and arms the device. The camera then detects a face through machine learning training. If the person isn&#39;t directly in front of the camera, the angle is calculated and the nerf gun is rotated to the correct position to fire. If the person is identified as unsafe, they are shot by the nerf gun.

![Level 1 Diagram](https://github.com/jdog453/Senior-Design-Project/blob/main/Design%20Diagrams/UpdatedD1.drawio.png)

This is our updated diagram. We decided to remove the webapp due to time constraints.

## Level 2

![Level 2 Diagram](https://github.com/jdog453/Senior-Design-Project/blob/main/Design%20Diagrams/D2.drawio.png)

The web app will have authentication to make sure that only certain users can access the app and activate the turret. A machine learning model will be trained for facial recognition. The current assumption is that there will be a free, publicly available dataset of faces to use for training. If not, the collection of images of faces to train and test the model with will be more tedious to produce. At this stage of development, we are also unsure of what type of machine learning model will be used for this task.

We plan to use pi cam (raspberry pi) as the camera: this device records video at 1080p 30 fps. Frames will be examined for the presence of a face. It will likely be computationally expensive to check every frame for this, so we will need to test and decide how many frames to ignore before checking a frame for facial detection.

Once a face is detected, the location of the person in comparison to the camera is calculated. This calculation is necessary as (obviously) the nerf gun will likely need to rotate to point at the target. At this stage of development, we plan to use a servo motor to do this. The output (a boolean value) is determined by whether or not the detected individual is unsafe. This value will represent whether or not the nerf gun should fire. An individual is defined as unsafe based on whether or not that individual&#39;s face has been recorded in our system. If he/she is identified as unsafe, the turret will fire at them. If the gun needs to be rotated it will rotate as the gun is firing.

![Level 2 Diagram](https://github.com/jdog453/Senior-Design-Project/blob/main/Design%20Diagrams/Updated%20D2.drawio.png)

This is our updated diagram. We removed the webapp due to time constraints. We also decided to use a webcam hooked up to a laptop instead of the pi cam due to processing power issues with the pi. Several versions of facial recognition are provided for the user ranging from purely facial detection and no recognition and both facial detection and recognition. The latter contains three variations ranging from a poor accuracy and great video performance to great accuracy and poor video performance. Video performance in this context refers to the the frames per second of the video stream. Two of the variations are very accurate due to the use of dlib's facial detection methods: HOG + Linear SVM face detector and CNN face detector. However, the use of these methods require a lengthy install of many features. information about this process is found in the user manual.

# Project Tasks and Timeline

## Task List

1. Research the most efficient machine learning model to implement facial recognition.
2. Investigate the existence of an available dataset of faces to train a machine learning model.
3. If a neural network is decided as the machine learning model, investigate the most efficient number of layers and neurons to use.
4. Develop software that identifies safe and hostile users based on camera frames and a ~~database~~ dataset of faces.
5. Develop a program to read the data from the camera
6. Develop a program to take the data read from the camera and feed it to the facial recognition software.
7. Research what language would work best for our project.
8. Design the stand for the turret.
9. Design the trigger pull system.
10. Design the hardware components of the aiming system.
11. Implement the calculations for the aiming system
12. Acquire a nerf gun.
13. Acquire ~~Raspberry Pi, Pi Cam, and motors~~ Arduino, web cam, and motors.
14. Build the turret.
15. Test the rotation system with the nerf gun mounted.
16. Test the trigger pull system.
17. Test the aiming system.
18. Test and validate the facial recognition system.
19. Document the software aspects.
20. Document the hardware aspects.
21. Design/Develop the web app.
22. Investigate which framework to use for the development of the web app
23. Investigation of how best to build the ~~database~~ dataset.
24. Build the ~~database~~ dataset.
25. Implement a user login system to activate the turret.

## Timeline

| Task # | Start Date | Completion Date | Milestone | Primary Responsibility | Completed |
| --- | --- | --- | --- | --- | --- |
| 1 | 12/11/2021 | 12/17/2021 | 1 | Austen | yes |
| 2 | 12/18/2021 | 12/24/2021 | 1 | Austen | yes |
| 3 | 12/25/2021 | 12/31/2021 | 1 | Austen | yes |
| 4 | 2/14/2022 | 3/1/2022 | 9 | Austen/Andrew | yes |
| 5 | 11/12/2021 | 12/31/2021 | 4 | Andrew | yes |
| 6 | 11/12/2021 | 12/31/2021 | 4 | Andrew | yes |
| 7 | 10/11/2021 | 11/11/2021 | 4 | Andrew | yes |
| 8 | 10/12/2021 | 11/6/2021 | 2 | Fred/Jared | yes |
| 9 | 10/12/2021 | 11/6/2021 | 2 | Fred/Jared | yes |
| 10 | 10/12/2021 | 11/6/2021 | 2 | Fred/Jared | yes |
| 11 | 1/31/2022 | 2/14/2022 | 7 | Austen/Andrew | yes |
| 12 | 10/11/2021 | 11/11/2021 | 3 | Jared | yes |
| 13 | 10/11/2021 | 11/11/2021 | 3 | Jared | yes |
| 14 | 11/12/2021 | 1/31/2022 | 5 | Fred/Jared | yes |
| 15 | 2/14/2022 | 2/22/2022 | 7 | All | yes |
| 16 | 2/14/2022 | 2/22/2022 | 7 | All | yes |
| 17 | 2/14/2022 | 2/22/2022 | 7 | All | yes |
| 18 | 2/23/2022 | 3/1/2022 | 9 | All | yes |
| 19 | 11/12/2021 | 4/1/2022 | 10 | Andrew | yes |
| 20 | 11/6/2021 | 11/11/2021 | 2 | Fred | yes |
| 21 | 12/6/2021 | 12/13/2021 | 6 | Andrew/Fred | no |
| 22 | 11/28/2021 | 12/05/2021 | 6 | Fred/Austen | yes |
| 23 | 12/14/2021 | 2/14/2022 | 8 | Jared | yes |
| 24 | 12/14/2021 | 2/14/2022 | 8 | Jared | yes |
| 25 | 12/6/2021 | 12/13/2021 | 6 | Fred | no |

## Effort Matrix

| Task | Andrew | Austen | Fred | Jared | Total |
| --- | --- | --- | --- | --- | --- |
| 1 | 15% | 75% | 5% | 5% | 100% |
| 2 | 15% | 75% | 5% | 5% | 100% |
| 3 | 15% | 75% | 5% | 5% | 100% |
| 4 | 15% | 75% | 5% | 5% | 100% |
| 5 | 75% | 15% | 5% | 5% | 100% |
| 6 | 75% | 15% | 5% | 5% | 100% |
| 7 | 75% | 15% | 5% | 5% | 100% |
| 8 | 5% | 5% | 45% | 45% | 100% |
| 9 | 5% | 5% | 45% | 45% | 100% |
| 10 | 5% | 5% | 45% | 45% | 100% |
| 11 | 85% | 5% | 5% | 5% | 100% |
| 12 | 0% | 0% | 0% | 100% | 100% |
| 13 | 5% | 5% | 5% | 85% | 100% |
| 14 | 5% | 5% | 45% | 45% | 100% |
| 15 | 25% | 25% | 25% | 25% | 100% |
| 16 | 25% | 25% | 25% | 25% | 100% |
| 17 | 25% | 25% | 25% | 25% | 100% |
| 18 | 25% | 25% | 25% | 25% | 100% |
| 19 | 45% | 45% | 5% | 5% | 100% |
| 20 | 5% | 5% | 85% | 5% | 100% |
| 21 | 45% | 5% | 45% | 5% | 100% |
| 22 | 45% | 5% | 45% | 5% | 100% |
| 23 | 5% | 5% | 5% | 85% | 100% |
| 24 | 5% | 15% | 5% | 75% | 100% |
| 25 | 5% | 5% | 85% | 5% | 100% |
| | 6.5 | 5.6 | 6 | 6.9 | |


# PPT Slideshow

[Senior Design Presentation](https://docs.google.com/presentation/d/1L0b7aCXFulL5tHAncLUut8ezNiC4T1P6QVw0lv1esw8/edit?usp=sharing)

# Final Results

Everything that we had time to do is finished and fully functional. Below we have a link to a folder showing our results. These videos include two scenario: one where Jared is identified as safe, and one where Jared is not identified as safe. For each scenario one video is the web cam footage that the turret uses to track and fire, and the other video is the perspective of a spectator. Any issues encountered during the development of this project can be found in the spring assessments.

[Project Result Videos](https://drive.google.com/drive/u/0/folders/1oBuupyKOHu9FiShU9h9XUVCafnCdbYtz)

# Summary of Hours

* Fall Semester:
    * Group work:
        * Senior Design Course Assignments:
            * 25 hrs
        * Misc:
            * 5 hrs brainstorming ideas and figuring out which devices to use
        * Total: 30 hrs
    * Individual:
        * Austen:
            * 4 hrs researching devices and examining different libraries
            * Total (including group work): 34 hours
        * Andrew:
            * 1 hr researching how to use python to rotate a servo
            * Total (including group work): 31 hours
        * Fred:
            * 2 hours researching how to modify nerf guns and assemble the turret.
            * Total (including group work): 32 hrs.
        * Jared:
            * 2 hours researching hardware we could use
            * Total (including group work): 32 hours
* Spring Semester:
    * Group work:
        * Senior Design Course Assignments:
            * 10 hrs
        * In-person meetings:
            * 3.5 hrs at freds 2/15
            * 5 hrs at freds 2/19
            * 1 hr slides at library 2/21
            * 2.5 hrs at freds 2/26
            * 3.5 hrs poster 3/2
            * 1 hr at freds 3/3
            * 1 hr spring break 3/15
            * 3 hrs at freds 3/22
            * 1.5 hrs freds 3/23
            * 5 hrs at jareds 3/25
            * 2 hrs jareds 4/6
        * Total:
            * 39 hrs

        

    * Individual:
        * Austen:
            * Per-week (13 weeks):
                * 4 hrs minimum
                    * Work included:
                        * Researching how to implement facial detection and recognition
                        * Researching how to best train the facial recognition model
                        * Developing facial detection and recognition
                        * Fine-tuning code and fixing bugs
                        * Implementing additional features to improve facial detection and recognition accuracy
                        * Working with different devices (raspberry pi, desktop computer, laptop)
            * Total per-week: 52 hrs
            * Total (including group work): 91 hrs
        * Andrew:
            * 8 hours working on getting the servos to respond to commands in python
            * 2 hours shopping for items to help attach stuff to the arduino
            * Total: 49 hours
        * Fred:
            * 4 hours of individual work making the poster look nicer. 
            * 5 hours learning how to disassemble the nerf gun, how its wires and mechanisms are set up, and how to reassemble it. 
            * 2 hours trying to figure out how to hijack the internal wiring of the gun to take an electrical signal from the arduino. 
            * 1 hour researching/shopping online for parts for the turret.
            * Total: 51 hrs.
        * Jared:
            * 3 hours getting equipment and brainstorming the turret
            * 10 hours of trial and error building the boxes and turret
            * 1 hour researching how the electronics physically work together
            * Total: 53 hours
* Overall Totals:
    * Austen:
        * 122 hours
    * Andrew:
        * 80 hours
    * Fred:
        * 83 hours
    * Jared:
        * 85 hours

# Self-Assessment Essays

## Andrew Dygert - Fall

The project that I will be working on is a nerf gun turret that will fire upon an individual in the appropriate circumstances. We plan to use a multitude of technologies to identify when the individual should be fired upon. These technologies include face recognition technology or some alternative to determine who is not a &quot;threat&quot;. There will also need to be a raspberry pi or some alternate so that we can program the machine. There is also the need for a mechanism that first the gun that will need to be fired. Lastly, there will need to be some override mechanic in case of a malfunction.

There are a few classes that will have taught us some things that we are going to need for this project. MATH1062 (Calculus II) and AP Physics C are going to be useful to do the calculations. In CS3003 (Programming Languages) we did some work with raspberry pi, which will be helpful, as well as some basic programming languages. In CS2028C (Data Structures), we learned about data structures that may be needed for this project. EECE3039C (Software Engineering) will also be very useful as a skill to help develop the software for the nerf turret. CS4033 (AI Principles and Applications) are also useful since it will be an AI firing and aiming the turret.

In my first co-op, I was a web developer for Learn 21. On my second co-op I was again a web developer, but with American Financial Group. My third co-op was with Cintas as a Data Analyst. These co-ops firstly taught me how to work well with a team, even if you are just meeting them for the first time. The first two web developer co-ops also taught me some SQL, which may be needed for this project. Lastly, my third co-op taught me machine learning, which may also be needed for this project.

I am excited about this project for several reasons. Firstly, this is the first major project I have been on that has a robotic element to it. I am also excited to use some facial recognition software, which seems to be more popular over time. I do believe our preliminary approach to the project will include some sort of facial recognition to identify people. I will also need some sort of robotic turret that can rotate, and angle up or down as needed. Then, depending on the results of the facial scan, it will decide whether to fire the nerf gun.

I expect that the nerf gun will be able to be fired with very good accuracy, especially from the range close enough to where the facial scan will have to take place. I believe that we can get the facial scan to work will. I am also worried about how precise robotics need to be, and if we can build them accordingly. I will evaluate my contributions, not only by the time I spend but by how much of that time I am getting quality work done and advancing our group towards our goal. We will know we are done when all parts are working, the firing of the gun is accurate, and the facial detection is also accurate. We will know whether we have done a good job is by how accurate the gun is, and how quick the gun is to fire.

## Andrew Dygert - Spring

My biggest individual contribution is the control of the turret. It was my job to be able to take the output from the facial recognition and determine whether the turret rotates to the left or the right, and whether it fires or not. I was able to get my part to work well from a coding, the biggest hurdle being how to get python to control what the Arduino powers, because the Arduino has its own language that is uses. Luckily there was a library to use that helped with the translation, and with some experimentation I figured out how to do it.  

I believe the only skill that I did not use was physics, but since the range on the nerf gun turret was far enough to cover any distance, it only needs to worry about rotation to aim. The other skills I mentioned were all used at least a little, with the most used skill being data structures, since the data types were different for the Arduino, I had to learn how they functioned. 

## Austen Brownfield - Fall

The senior design project my group and I are currently expecting to research/build is a
nerf gun turret that will fire upon individuals in specific circumstances. These circumstances
include if the face of an individual is detected on a camera, or if a motion sensor is tripped. This
group consists of only computer science students, so I believe an area we???re all strong in is
software development and programming. I believe this experience will allow us to successfully
develop software that can perform some of the necessary tasks for this project (e.g. use machine
learning to identify faces, control when the nerf gun fires, etc.). However, I believe my group and
I lack experience with physical hardware and devices, so some aspects of this idea (pulling the
trigger, creating/monitoring a motion sensor, etc.) may be difficult to implement.

I???ve personally taken specific courses at this university that I think will provide a good
foundation for the experience/information needed to complete this project. I???ve taken
MATH1062 (Calculus II), MATH2076 (Linear Algebra), CS4033 (AI Principles and
Applications), and CS5137 (Machine Learning). I believe, if my group were to implement some
form of machine learning for facial recognition, the knowledge I???ve gained from these courses
will allow me to implement this. I???ve also taken many programming courses such as
EECE3093C (Software Engineering), CS3003 (Programming Languages), CS2021 (Python
Programming). I think these courses gave me the necessary experience I???ll need to create and
implement code for this project. I???ve also picked up skills and experience from my coops.

I worked at the tech company London Computer Systems for four semesters. My position
was that of a quality assurance software tester for one semester. During this time, I discovered
and reported defects to my team, coordinated with software developers to verify code changes
had addressed certain issues, and was responsible for creating and executing test cases. I was a
software developer for the other three semesters of my coop. In this position, I reviewed software
changes made by others to ensure program quality and designed, developed, and implemented
code changes to software. I also gained experience working with a team of competent software
developers. I believe my time spent on coop provided me with efficient software development
skills and practices as well as good testing habits that will allow me and my team to competently
work on and complete this project.

I???m excited to work on this project for several reasons. The first of which is that I feel
like this is the best opportunity I???ll have at university to create something that not only am I
proud of, but something my friends and family can be proud of too. This project could be a neat
feather in my cap that tells others I learned something at school and made something awesome
with it. Secondly, I think this project idea is difficult enough that my team and I can pick up new
skills along the way. For example, like I said earlier, I feel the software aspect of this project
won???t be too difficult, but the hardware aspect (pulling the nerf gun trigger, creating/monitoring a
motion sensor, etc.) is something I do not know very well at all. However, I think researching
this and coming up with our own solutions will be a great opportunity to learn about subjects that
weren???t present in our traditional CS curriculum. I think our preliminary approach to this project
will be deciding what aspects of this are absolutely necessary to include and which aspects
aren???t. For example, should we design and build a track that moves and adjusts the angle of the
nerf gun depending on the position of whoever is spotted on camera? If so, how will that be done
and can it be done in an efficient way that won???t take months to complete? Otherwise, let???s adjust
the parameters of our project so we don???t need to implement the track specifically and can
instead focus on the bigger picture.

At this point, the only expected result that I wish for this project is that the nerf gun will
fire when someone has been detected via facial recognition or a motion sensor being tripped. I???m
not sure of the smaller, more specific results that I wish to see since my group and I haven???t
discussed them yet. I???ll personally evaluate my contributions by objective metrics such as the
total amount of time I spent working on this project and how many lines of code I???ve written. I???ll
use more subjective metrics such as how often I was able to successfully help group members
complete their work, or how others feel and view our project as time progresses too. Besides the
obvious deadline date, my group and I will know when we???re done once the project has
successfully completed the goals we set for it. If our project can do that, and it was able to do
that with little sacrifice to what we originally wanted to do, then I would feel that I had done a
good job creating this project

## Austen Brownfield - Spring

My individual contribution to this project was the research, development, and implementation of facial detection and recognition. The required skills previously identified to perform these tasks were applied and built upon in order to successfully create this aspect of our project. A significant portion of time was spent researching these topics. Research included what languages, libraries, and references to use. The site PyImageSearch was instrumental in my research as it allowed me to build the base of several versions of detection and recognition. Additional code for other aspects of the project were created in conjunction with detection and recognition such as the rotation and the firing of the nerf gun. The code was written in Python on Jupyter notebooks, and stored in our team???s Github repository. I gained experience with Python libraries such as OpenCV, dlib, and face_recognition, and grew more familiar with the use of Jupyter projects and the Raspberry Pi device. My understanding of facial detection and recognition algorithms and their computational complexities has also increased. I???ve developed greater skills working on a team and with tools such as Github.

I was able to successfully implement facial detection and several versions of facial recognition ranging from poor accuracy and efficient video performance to great accuracy and inefficient video performance. Video performance refers to the frames-per-second of a videostream. There were many obstacles along the way. A significant portion of time was spent researching how these goals could be achieved on a Raspberry Pi only for the device???s usage to be scrapped due to how poor its performance was. The development of an accurate facial recognition model was difficult as the solution was tedious and poorly documented. A ???CUDA-compatible??? GPU was required to use a more accurate model; however, resources explaining the process of installing the proper tools were not forthcoming and required much research. Only a fraction of our group???s computers met this requirement and the amount of devices that could be used for testing were limited.

I believe my group accomplished the significant goals we created for our project in the Fall. This includes the firing of the nerf gun, the rotation of the device based on the location of one???s face on camera, and the detection and recognition of the face. There were many sub-goals along the way such as the research and acquisition of the parts, the creation of the physical device that holds the nerf gun, the development of the device to physically pull the trigger, the implementation of the software that implements the rotation, etc. I further learned how necessary it is for the work associated with large projects to be divided amongst a team in order to more quickly accomplish goals. A successful aspect of our teamwork was that the team members all felt comfortable with each other and were willing to ask for help and discuss setbacks. An unsuccessful part of our teamwork was that we were initially unaware of the amount of work required for each task, and some team members were given comparatively more work than others to complete. This led to some confusion, frustration, and reorganization further into development.

I think my efforts may have been greater than others on my team. However, I believe this is because the work I was given was more complex and involved than others. I was also very interested and passionate about my work that I didn???t mind spending extra time ensuring that my items were as perfect as possible given our time and resources. My team member Jared Musser spent a large amount of time building the device that held the nerf gun and I think that deserves special recognition given that our team is wholly Computer Science and that the more physical ???hardware??? problems aren???t usually a part of our work.



## Fred Jenks - Fall

Our planned project involves using facial recognition and motion tracking to create a sort of automated defense system. We plan to write a program that takes one or more camera feeds as input. When the program &quot;spots&quot; a face that is not authorized, it will fire at that face. As for the physical aspect, we plan to use a nerf gun and a set of motors to aim and fire it. The facial recognition will likely utilize machine learning to train the program to tell what is a face and what isn&#39;t. If the facial recognition fails, we plan on using motion sensors as a backup. We want to combine these inputs, feed them to a program, and have it accurately determine if there is an unauthorized person approaching.

So far in our curriculum, we have had a couple classes that will assist us with this project. The biggest help will be from our Principles of A.I. class (CS 4033), as that will assist us with the machine learning knowledge that we will need to train the program. Hopefully, that knowledge will not be overly difficult to apply to facial recognition. Also helpful will be our Python Programming class (CS 2021), as the library we used for CS 4033 was in python so we will likely have to use it quite a bit. Finally, I think my current Requirements Engineering class (CS 5127) will be very helpful for us. Being able to accurately determine what we need to do will be very important for making sure this project gets done.

As for my co-op experiences, I&#39;m honestly not sure how much help they&#39;ll be. I spent my last four rotations as a C# Developer at Edaptive Computing, Inc. If our project ends up needing any work in C#, then I&#39;ll likely be able to handle it. In addition to the C# work I did, most of my projects involved webapp development, so HTML, JS, and a little bit of TypeScript towards the end. I also did some work in SQL, which we will likely need. Outside of coding, I worked in small agile teams, which meant that even as an intern I had responsibilities in our meetings, whether they be for peer review, sprint review, or sprint planning. I also did a lot of work on documentation for each of my projects, which has greatly improved my technical writing skills.

Our preliminary approach will be to build a sort of stand for the gun to sit on, which will hopefully be able to adjust itself to aim the weapon if we have time to implement aiming. We will also set up a network of cameras and motion sensors so that the turret knows if someone is approaching. We will also need a mechanism to pull the trigger. If we have time for aiming, we will use the sensors and a set of motors to aim the gun. Our expected result at the end is to have a functional turret that can detect a person approaching, and if their face is not recognized or authorized, then the gun will fire. I will evaluate myself based on if what I&#39;ve done has made major contributions to the project and if the project is a success. If both are true, I&#39;d consider it a job well done.

I am excited for this project for a few reasons. First and foremost, machine learning is a major thing right now, so doing as much work with it as possible is important in my opinion. Facial recognition is also big with a lot of companies right now, so learning how to do it would be helpful for job searches, on top of it being a very cool innovation. On top of the real world applications of our project, it sounded like a lot of fun to make. I expect to come out of this project with a much better knowledge of how machine learning and facial recognition work, as well as a strong understanding of how to set them up to live camera feeds and determine who it&#39;s seeing in real time. I also am excited to learn about all of the physical aspects, such as hooking up the motion sensors, building the stand, and setting up the motors to aim if time permits. This project sounded great to me when it was proposed by one of my groupmates, and I can&#39;t wait to get started.

## Fred Jenks - Spring
My individual contribution to the project was originally meant to be setting up the internal wiring of the gun to take the signal from the Arduino to fire. However, due to the modification safeguards implemented by the manufacturer made it difficult to mess with the wires, we decided to scrap that idea because we didn???t want to risk breaking the gun. My other semi-major contribution, the webapp that was to be linked to the turret, was also dropped due to time issues. After these decisions, I took on more of a ???everyman??? role assisting where I could, such as writing the script to split videos into images for model training or designing the poster for the expo. 

I think I did build on the skills identified last fall, as we did a lot of python programming and learned a lot about the libraries we used. I think I rebuilt my competency with Arduino, as it???s something I???ve worked with previously but not much lately. I also learned how to use Jupyter notebooks, and built on my previous Python experience. My major successes were getting the poster made and looking nice and writing the video split script. My major obstacles were the wiring issues and the amount of time spent disassembling the gun and learning about its inner mechanics.



## Jared Musser - Fall

Our proposed project is to build a nerf turret that utilizes facial recognition software that we develop. This system will &quot;spot&quot; a face that it doesn&#39;t recognize and will then fire at the unsuspecting victim. We all are computer science students so we all have sufficient programming knowledge and experience to write the software. I think we will learn applicable skills such as machine learning for facial recognition and different things related to pulling the trigger and controlling when the trigger gets pulled. We all may have a bit of a lack in the hardware department since we are all computer science, however I have used Raspberry Pis and Arduinos in a previous class as well as a club I was in that developed a high altitude balloon payload and mission and used both an Arduino and a Raspberry Pi for the payload. But I may have some knowledge on how to use these small PCB&#39;s to manage the physical system.

One of the main things that goes into getting this turret to work is a working AI that uses a camera input to determine if a person is recognized or not. I think the class CS 4033 AI: Principles and Applications will help with laying the groundwork for the AI as well as the dirty work of getting it to work. Another class that will be used is EECE 3093C Software Engineering. This class should be the guide to creating our software. A class that I&#39;m currently in I think could help, it is CS 5127 Requirements Engineering. It should provide some general understanding of the structure of our project and the way to tackle the problem we are trying to solve.

During my co-op I learned some skills that I think will come in handy during this project. Non-technical skills that I learned such as communication and leadership on a project will help move this project along well and will help with working with people on this project. I worked on an application essentially by myself. I was given a web that had the bare bones and I pretty much made the application. I think my knowledge from actually working will also help. In the technical sense I am a Microsoft Certified Professional in C#. I received this certificate after months of preparing for the exam. I think this could help with the back-end, dirty work of the application. In the web apps that I made on c-op C# was the dirty work of the application, the back-end code that manipulated data, connected to databases, and I think that could help me to make the dirty work or back-end stuff working. My co-op job was as a Web Developer. I worked at a small consulting company in West Chester called Fortech LLC.

I am excited about this project for a couple reasons. One of these reasons is that I am genuinely passionate about security. Not necessarily safety, but like security for our nation, my home, and my family. I think this project will give me just a small taste into developing security systems and solutions to potential safety and security issues. I plan on making my own things relating to this, but more complex and for various things. Another reason I am excited to work on this project is that it is going to be the thing I think I will remember the most from my classes and accomplishments while in college. This project can and will be something that I can be proud of, my teammates can be proud of, and our families can be proud of. I think these projects should have aspects of these things and should be fun and interesting for everyone involved as well. This will definitely be fun to build and test out and mess around with. The preliminary approach we have for this project is to determine everything we will need and won&#39;t need and what could potentially be cut from a final design to minimize cost and still make a good product.

My expectations for this project are that we are going to be able to detect an unknown face and fire the nerf gun. Specifics for each person that I hope to see are currently unknown as nothing in this regard has been discussed. I think I will be evaluating myself and contributions based on how much code I&#39;ve written, how much time I spent on the project, and how much of the physical turret is built and eventually functional. There may be things that I do in a subjective manner such as if I was able to help the rest of the group on their part of the code or in the case of the other turret builder how much we help each other in building it I guess. I may also evaluate how the rest of my group feels about their work and views the project and time and the project progress. I think using a date to say when something is done isn&#39;t a good way to say something is done. I think to say it is done means different things. It could be code without bugs, it could be when initial requirements are met, it could be a whole host of things. However, I think for us to say our project is done probably falls in line with the initial requirements being met. Once these requirements (or goals) are met and it is with as little as possible sacrifice from the original goal and is successfully working, we can say we did a good job and our project is complete.

## Jared Musser - Spring

Most of the work I performed on the project was physical work. Initially the plan for my work was split between making a database for our software to store safe faces and building the turret. When someone else was working on the facial recognition we discovered that the database I was going to create was unnecessary because the python library we used had one built into it for the safe faces. The idea of the physical turret was to have a box that the gun sat in that used a servo to turn on another box and wire the gun to an Arduino to send it signals to shoot. After we determined we couldn???t wire the Arduino directly to the gun we decided to make a trigger pulling system with a servo and twine that we turn to pull the trigger. In order to create the boxes I used power tools to cut the wood to size and make the boxes. 

I became more confident with power tools. I can???t say I learned too much programming wise since my software part of the project got canned. Only two of us ended up having software parts to the project. I???m not the happiest about it because I feel like I did nothing to get it functional. All I did was physical work. I wish I would have done more programming work. That was definitely an obstacle, more so a mental one though. I needed to so some processing to be okay with not doing any programming. I have had interviews ask about my part in the project and I don???t have much to tell since I didn???t write any code. There were many physical challenges though that all center around making the box the correct size and modifying the gun to fit and stuff. There were several meetings we had that I needed to re-think the box, the friction when it turned, and other physical problems. It took at a lot of mental power and trial and error to get it pretty much right. There are still improvements that could be made to make it more functional.

# Professional Biographies

## Andrew Dygert

Bio:

I am a Computer Science major with 3 separate co-op experiences. In my first co-op, I had a great experience, was unfortunately only able to stay with them for a semester. My next co-op had a similar experience despite the first, even though the second company was much larger than the first. The co-op also came to an early end due to Covid-19. Also because of Covid, I was unable to find another co-op until the Summer of 2021 with Cintas. This was a completely new experience than the first two in both technologies and culture. It ended a little shorter than I would have liked, so I wasn&#39;t able to finish the last project I was working on. Outside of my jobs and classes, I do enjoy sports, listening to music, video games, and occasionally coding solutions to some (usually not so serious) problems I encounter in my life.

Contact Info:

- Email: [dygertaj@mail.uc.edu](mailto:dygertaj@mail.uc.edu)
- Phone: 513-255-3470

Co-op Experience

- Cintas
  - Intern, Sum. 2021
  - Data Analytics and Machine Learning
  - SQL
  - Used SAP technologies
  - Began project to help identify potential customers using machine learning
- American Financial Group
  - Intern, Fall 2019
  - Web Development in ASP.net
  - C#, JavaScript, HTML, CSS
  - Helped develop improvements to the company&#39;s internal website
- Learn21
  - Intern, Spring 2019a
  - Web Development in ASP.net
  - C#, JavaScript, HTML, CSS
  - Developed a website to track the application process for a client&#39;s school

## Austen Brownfield

**Contact Information**

- Email: [Brownfaw@mail.uc.edu](mailto:Brownfaw@mail.uc.edu)
- Phone: (614) 398-6430

**Co-op and other related experiences**

- Software Developer, London Computer Systems, Mason, Ohio. (3 semesters)
  - Reviewed code changes to ensure program quality
  - Designed, developed and implemented code changes to software
  - Experience collaborating with a team of software developers
  - Responsible for converting sections of desktop client to web application
  - Created code changes primarily for front-end of web application
- QA Software Tester, London Computer Systems, Mason, Ohio (1 semester)
  - Discovered and reported defects. Coordinated with software developers to verify code changes addressed software defects
  - Responsible for creating and executing test cases and regression testing.

**Skills/expertise areas**

- Programming: C++, Python, TypeScript
- Operating Systems: Windows
- Web Development: HTML, CSS, Angular
- Database Programming: SQL
- Software: Adobe Photoshop, Adobe Premiere, Microsoft Office Professional including Excel, Word and PowerPoint

**Areas of interest**

- Machine Learning
- Cyber Security
- Game Development
- Web Development

**Type of project sought:**

- Develop a game that utilizes machine learning to some extent.
- Implement machine learning to aid in some form of cyber security problems.
- Create a website that demonstrates potential usage of machine learning through practical examples.

## Fred Jenks

**Bio:**

I am a Computer Science major fresh off my 5th co-op term. I spent my first semester at Siemens, which didn&#39;t really go as planned. After that, I went to Edaptive Computing, Inc. for my last 4 semesters, as well as some part-time work there while I was in classes last fall. While there, I worked mostly on web apps, generally using C# with Entity Framework, JS, and HTML with a quick pit stop in a project using TypeScript and SQL and some work with CentOS 7 and Docker. Outside of work, I enjoy watching/playing sports(go Browns!), video games, listening to music, and working on computers.

**Contact Info:**

You can get to me by:

- Email: [jenksfc@mail.uc.edu](mailto:jenksfc@mail.uc.edu)
- Phone: 614-726-2426

**Co-op Experience:**

- Siemens Software, Inc
  - Intern, Spr. 2019
  - Angular, C#
  - Small Team Agile
- Edaptive Computing, Inc
  - Intern, Fall 2019, Sum 2020 - Sum 2021
  - C#, NodeJS, HTML, CSS, TypeScript, SQL, Linux Kernel
  - Small Team Agile
  - End User and Developer Documentation

**Projects Sought:**

- Web Development
- Game Development
- Machine Learning
- Preferably something cool

## Jared Musser

**Contact Information:**

- Email: [musserjl@mail.uc.edu](mailto:musserjl@mail.uc.edu)
- Phone: 513-315-4637

**Co-op Work Experience:**

- Web Developer, Fortech LLC, Jan. 2019-May 2019, Aug. 2019-Dec. 2019, May 2020-Aug. 2020, Jan. 2021-Aug. 2021

  - Used JavaScript, C#, HTML, CSS, and SQL to write web applications for customers and internal company uses.
  - I learned different JavaScript frameworks for this applications, namely react.js, node.js, and vue.js.
  - Database work included writing stored procedures, maintaining the server it was on, and writing complex SQL queries.
  - Most of my work was on my own and my own projects, however, I did get some help some of the semesters from senior developers when I needed it.
  - During the summer semester of 2020 (May to August of 2020) I got certified in C# by Microsoft.
  - The double rotation when I was working there for nearly 8 months, I was given a project where the groundwork was laid out and I wrote essentially the entire application minus a couple things. I did almost all the bug fixes that happened. Another co-op was tasked to help me with bug fixes and quick enhancements.
  - During that application I created a custom renderer that took data in as a parameter and created a custom way to put the data in a tree format.
  - I also learned the more complex technical side to vue during this project as well. I used vue previously, but not as in depth and complex as with this application.

**Skills:**

- C#, C++
- JavaScript, Vue
- Python
- HTML, CSS
- SQL

**Project Sought:**

- Game Development Related
- Web Development
- Maybe VR Simulation or something similar

# Poster
https://github.com/jdog453/Senior-Design-Project/blob/main/FinalPoster.pdf

# Budget

$100 - Test Guns and Darts

$162.57 - Raspberry Pi, PiCam, Servo, hardware to get things working together

# Appendix

Proof of 45 hours

The effort matrix sums the contributions of each team member in regard to the total contributions. The lowest contribution among team members is 5.6 (~22%). The total number of days that make up the major tasks of this contribution are ~35. Assuming 1.5 hours of work are done each of these 35 days, this member will contribute 52.5 hours of work towards this project&#39;s completion. It&#39;s unrealistic that the upper bound of each group member&#39;s work for a day is 1.5 -- this total will likely be much higher. Also, when taking into account the activities that this group member isn&#39;t majorly contributing to, as well as the shared work of all tasks across this project among all team members, easily over 50 hours of work will be performed.

Assuming that this same calculation can be performed for each group member, and considering the total contribution percentage of every other group member is larger than the previously discussed member, then every group member will easily contribute over 45 hours of work across this project&#39;s duration.
