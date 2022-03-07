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

    def align_faces(self, image, imagePath):
        fa = FaceAligner(self.predictor, desiredFaceWidth=256)
        # load the input image, resize it, and convert it to grayscale
        image = imutils.resize(image, width=800)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # A list of rectangle elements are returned. Each rectangle represents the coordinates of a bounding box around
        # a face that was detected in the image.
        rects = self.detector(gray, 2)
        # We assume that only one face per image. Should more be found, a message is printed.
        if len(rects) > 1:
            print("Multiple faces found in image: {}!".format(imagePath))
        # The first bounding box is aligned face is returned.
        return fa.align(image, gray, rects[0])            