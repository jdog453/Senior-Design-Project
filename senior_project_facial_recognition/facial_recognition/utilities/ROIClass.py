# Each ROI (face) found in a frame will be stored as an ROIFace object.
class ROIFace:
    def __init__(self, startX, startY, endX, endY, center):
        # The coords represent the startX, startY, endX, and endY
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY
        self.dist_from_center = self.calc_dist_from_center(center)
    
    def calc_dist_from_center(self, center):
        # If the center of the frame is within the ROI's bounding box, then the distance is returned as 0.
        if center < self.endX and center > self.startX:
            return 0
        # Else, the minimum value of the distance between the center and either the startX or endX value is returned.
        return min(abs(center - self.startX), abs(center - self.endX))
    
    def __gt__(self, other):
        # Given a list/array of ROIFace objects, they are sorted based on the distance_from_center
        return self.dist_from_center > other.dist_from_center
            
        