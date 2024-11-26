
#Lscale-invariant​\=n1​i∑​(log(yi​)−log(y^​i​))2−2n21​(i∑​(log(yi​)−log(y^​i​)))2

from dataclasses import dataclass
import cv2
import numpy.typing as npt
import math
from datetime import datetime
from tqdm import tqdm

@dataclass
class Image:
    Depth: npt.NDArray
    Pred: npt.NDArray
    Shape: tuple

class L2_Scale_Invariant():
    def __init__(self, depth, depth_pred):
        self.images = self.read_images(depth, depth_pred)
        self.timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    def read_images(self, depth, pred) -> Image:
        try:
            depth, pred = cv2.imread(depth, cv2.IMREAD_GRAYSCALE), cv2.imread(pred, cv2.IMREAD_GRAYSCALE)
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
        squared_diff_list, diff = [], []
        for h in tqdm(range(images.Shape[0])):
            for w in range(images.Shape[1]):
                i, s_constant = (h, w), 1e-9
                depth_value, pred_value = images.Depth[i], images.Pred[i]
                if depth_value == 0 or pred_value == 0:
                    difference = math.log10(depth_value + s_constant) - math.log10(pred_value)
                else:
                    difference = math.log10(depth_value) - math.log10(pred_value)
                with open(f'log-{self.timestamp}.txt', 'a') as file:
                    file.write(f"Coordinates: {i}, Values: (V1={depth_value} V2={pred_value}), Diff={difference} \n")
                    file.close()
                squared_diff = difference ** 2
                squared_diff_list.append(squared_diff)
                diff.append(difference)
        return squared_diff_list, diff

    def mean_calc(self, squared_diff, diff, n):
        total_sum_squared, total_sum = sum(squared_diff), sum(diff)
        squared_mean = total_sum_squared / n
        mean = total_sum / n
        return squared_mean, mean

    def term_calc(self, squared_mean, mean, n):
        total_1 = (1 / n) * squared_mean
        total_2 = ((1 / (2 * n) * mean) ** 2)
        total = total_1 - total_2
        return total

    def calculate(self):
        images = self.images
        n = len(images.Depth)
        squared_diff, diff = self.get_pixel()
        squared_mean, mean = self.mean_calc(squared_diff, diff, n)
        total = self.term_calc(squared_mean, mean, n)
        return total
        
if __name__ == "__main__":
    IMG_PATH_GROUND = "mi_0.png"
    IMG_PATH_PRED = "zo_0.png"
    total = L2_Scale_Invariant(IMG_PATH_GROUND, IMG_PATH_PRED).calculate()
    print(total)
        

