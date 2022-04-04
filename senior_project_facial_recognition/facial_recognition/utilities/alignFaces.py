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
        self.fa = FaceAligner(self.predictor, desiredFaceWidth=256)

    def align_faces(self, image):
        # The input imageis loaded, resized, and converted to grayscale
        image = imutils.resize(image, width=750)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Each rect represents the coordinates of a detected face's bounding box.
        rects = self.detector(gray, 2)
        
        if len(rects) > 1:
            print("[INFO] multiple detections in image being aligned.")
            
        for rect in rects:
            # Only the first detection is returned.
            return self.fa.align(image, gray, rect)
        
        # If there were no detections, then the original image is resized and returned.
        print("[INFO] no detections found in image. Returning original.")
        return imutils.resize(image, width=256)