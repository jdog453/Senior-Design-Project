from imutils.face_utils import FaceAligner
from imutils.face_utils import rect_to_bb
import imutils
import dlib
import cv2
import sys

# This class is responsible for aligning the faces of the passed input images.
class AlignFaces:
    def __init__(self):
        # The detector and predictor are initialized.
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor("../../facial_detection/models/shape_predictor_68_face_landmarks.dat")

    def align_faces(self, image):
        fa = FaceAligner(self.predictor, desiredFaceWidth=256)
        # load the input image, resize it, and convert it to grayscale
        image = imutils.resize(image, width=800)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # A list of rectangle elements are returned. Each rectangle represents the coordinates of a bounding box around
        # a face that was detected in the image.
        rects = self.detector(gray, 2)
        if len(rects) > 0: # check that at least one face is detected within the image.
            if len(rects) > 1:
                print("[INFO] multiple detections in image being aligned.")
            # The first bounding box is aligned and the face is returned.
            return fa.align(image, gray, rects[0])
        else:
            print("[INFO] no detections found in image. Returning original.")
            return image # if no detections were found, then the original image is returned