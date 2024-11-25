
#Lscale-invariant​\=n1​i∑​(log(yi​)−log(y^​i​))2−2n21​(i∑​(log(yi​)−log(y^​i​)))2

'''L2 Scale Pre-optimization
logic for images. 
'''


"""
read 2 images -> grayscale (depth, depth_pred)
take perimeter, get total pixels
(h,w) 

"""

from dataclasses import dataclass
import cv2
import numpy.typing as npt
import math

@dataclass
class Image:
    Depth: npt.NDArray
    Pred: npt.NDArray
    Shape: tuple

def L2_Scale_Invariant():
    def __init__(self, depth, depth_pred):
        self.images = self.read_images(depth, depth_pred)

    def read_images(self, depth, pred) -> Image:
        try:
            depth, pred = cv2.imread(self.depth, cv2.IMREAD_GRAYSCALE), cv2.imread(self.depth_pred, cv2.IMREAD_GRAYSCALE)
            depth_shape, pred_shape = depth.shape, pred.shape
            if depth_shape != pred_shape:
                ValueError
            else:
                shape = depth_shape
            return Image(Depth=depth, Pred=pred, Shape=shape)
        except Exception as e:
            print(e)
    
    def get_pixel(self):
        images = self.images

        for h in images.Shape[0]:
            for w in images.Shape[1]:
                i = (h, w)
                depth_value, pred_value = images.Depth[i], images.Pred[i]
                difference = math.log10(depth_value) - math.log10(pred_value)
                squared_diff = difference ** 2
        return squared_diff
                
    def calculate(self):
        images = self.images
        for h in images.Shape[0]:
            for w in images.Shape[1]:
                

        

