
# User Documentation and User Manual
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
            * Senior-Design-Project > senior_project_facial_recognition > …
                * facial_detection
                    * This is only facial detection. There is no recognition. This means that there is no training on “safe” faces and that the nerf gun turret will blast at anyone indiscriminately
                * facial_recognition
                    * This uses facial recognition but with a less-than-ideal model (i.e., the accuracy of the model is not the best).
                    * However, this should be used if:
                        * The user does not have a CUDA compatible GPU
                    * Although much less accurate than the below version, this can be used without GPU support.
                * facial_recognition_V2
                    * There are two versions of this software that can be used. Both are found within the same file. The user simply changes the “detection_method” input parameter to be:
                        * hog
                            * Less accurate than cnn, but quicker to encode the faces and better fps of the video stream
                        * cnn
                            * More accurate than hog, but takes longer to encode the faces and slightly worse fps in video stream
                    * If the user’s GPU is CUDA compatible and the GPU is “good” then this method should be used.
        * What’s needed for all versions:
            * Python
                * The 64-bit version was used for this project.
                    * The 32-bit version was never tested. However, the assumption is that downloading the 32-bit libraries for the other packages should allow this to work.
                    * Instructions will continue by outlining the libraries used with the 64-bit version of Python
            * Windows OS
                * This was not tested on another OS. As such, the instructions will only be for this OS.
            * Opencv-python 4.3.0.38
            * Face-recognition library
            * Imutils library
        * The instructions below are for the “V2” version of facial recognition.
            * The steps to set this up are very involved, time-consuming, and needlessly obtuse. However, I’ve tried to compile all of the resources I used to set this up on my machine to make things easier:
                * Install Visual Studio (2019)
                    * Other versions will likely work as well.
                    * In the “Visual Studio Installer” application:
                        * Select “modify”
                        * Along the right panel, drop the “Desktop Development with C++” menu
                        * Among the already-selected items (if any), ensure that the following are selected:
                            * Windows 10 SDK
                            * C++ CMake tools for Windows
                            * MSVC build tools
                        * Select “modify”
                * Install CMake
                * Install Anaconda
                * Install NVIDIA CUDA Toolkit and cuDNN:
                    * Instructions to set this up can be found on the site:
                        * [https://medium.com/analytics-vidhya/cuda-toolkit-on-windows-10-20244437e036](https://medium.com/analytics-vidhya/cuda-toolkit-on-windows-10-20244437e036)
                    * Additional instructions to help with the process:
                        * [https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html)
                        * [https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html) 
                * Install dlib using conda with CUDA enabled:
                    * Follow the below instructions **up to but not including the “nvcc” part:**
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
                            * Edit the "C:\ProgramData\Anaconda3\Scripts\activate.bat" file and add the following before the first “@if”:

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
        * To power off the turret, click the “q” key while the stream is up. This will close the stream and end the program.
    * Train the facial recognition model to recognize specific faces.
        * The facial recognition model needs to be trained with the faces that you wish to be marked as “safe”. This training is done by providing the model with pictures of these faces. The more pictures, the more accurate the model. The model needs to be retrained every time a new face is added/removed from the list of safe faces.
        * The pictures should be of one’s face as the face is directly facing the camera.
        * There should be at least 6 pictures and at most 100 pictures of the same person’s face.
        * The user must manually insert a directory representing a face.
            * Navigate to “Senior-Design-Project/senior_project_facial_recognition/facial_recognition_data/faces_dataset”
            * Create a directory with the name of the person who wishes to be marked as safe.
                * E.g. should the user wish to train the model with pictures of a face belonging to an individual named “Ben,” then the directory will be called “ben”
            * Within this directory, insert pictures of this individual’s face.
                * The file format of each image can be either png or jpeg
                * Note: We’ve also included a script that will take a video and read its frames. These frames can be used as images for the directory. See _Collecting Pictures** **_section.
        * Once the directory has been updated, embeddings must be generated for each face. This is a necessary step to train the model to recognize the faces.
        * Senior-Design-Project > senior_project_facial_recognition > facial_recognition:
            * Navigate to “Senior-Design-Project/senior_project_facial_recognition/facial_recognition/notebooks/extract_embeddings.ipynb” and run the code.
                * The data parameters do not need to be adjusted for this.
            * Once this step completes, the model must be trained with the data generated from the previous step.
            * Navigate to “Senior-Design-Project/senior_project_facial_recognition/facial_recognition/notebooks/train_model.ipynb” and run the code.
                * The data parameters do not need to be adjusted for this.
            * Once trained, the stream can be started.
            * Navigate to “Senior-Design-Project/senior_project_facial_recognition/facial_recognition/notebooks/recognize_stream.ipynb” and run the code.
                * It may take some time (~1-2 mins) for the stream to begin.
                * Once the stream begins, a window will open on the user’s machine. This window shows the live feed from the stream.
            * The stream should begin and the turret is on.
            * To power off the turret, click the “q” key while the stream is up. This will close the stream and end the program.
        * Senior-Design-Project > senior_project_facial_recognition > facial_recognition_V2
            * Navigate to Senior-Design-Project > senior_project_facial_recognition > facial_recognition_V2 > notebooks > encode_faces.ipynb
                * Adjust the “detection_method” data parameter based on which implementation you’d like to use. The other parameters do not need to be adjusted.
            * Once this completes, the stream can be viewed.
            * Navigate to Senior-Design-Project > senior_project_facial_recognition > facial_recognition_V2 > notebooks > recognize_faces_stream.ipynb
                * Adjust the “detection_method” data parameter based on which implementation you’d like to use. The other parameters do not need to be adjusted.
            * The stream should begin and the turret is on.
            * To power off the turret, click the “q” key while the stream is up. This will close the stream and end the program.
    * Collecting Pictures
        * The process of collecting pictures for an individual can be long and tedious depending on how many pictures one wishes to use. We’ve added a script to help with this process.
        * First, record a video of the individual you wish to train. This video should be of the individual’s face close to the camera with no other items elsewhere that look like faces.
            * The video length does not matter too much. If you wish to collect x pictures from a video that contains &lt; x frames, then an error will occur. The longer the video, the more spread out the pictures from the video that will be used to train the model will be.
        * Navigate to “Senior-Design-Project/senior_project_facial_recognition/facial_recognition_data/utilities/vid_split.ipynb”
            * Change the “input_path” parameter to the input path of the video.
            * Change the “max_pictures” parameter to an integer representing the max amount of pictures you’d like to take from the video
            * Change the “output_dir” parameter to the directory of where the pictures should be saved.
                * This should be to directory that was created for the individual you’d like to train the model on
            * Change the “file_pre_name” parameter to the text that you’d like to be prepended to the file name.
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
        * Try to add the person’s face to the model again and retrain it.
        * Facial recognition models are never 100% accurate. A good rule of thumb is that the more data there is to recognize a person, the better the model will be.
    * Why does the nerf gun turret not fire at people who are not marked as safe?
        * Make sure the camera’s lens is clean, and that the gun’s batteries are not dead.
    * Why is the nerf gun turret not aiming? Alternatively, when the nerf gun turret aims, why does it aim slowly?
        * Make sure that the servo motor battery packs are not dead.
