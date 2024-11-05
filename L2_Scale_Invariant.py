import math
import numpy as np 


class L2_Scale_Invariant():
    def __init__(self, ground_truth, predictions):
        self.ground_truth = ground_truth
        self.predictions = predictions
        self.n = len(self.ground_truth)

    def side_a(self):
        diff_list = []
        for i in range(self.n):
            difference = (self.ground_truth[i] - self.predictions[i])
            diff_list.append(difference)

        #Find the sum of all values:
        diff_sum = sum(diff_list)
        print(diff_list)

        neg_value = []
        for number in diff_list:
            if number < 0: 
                neg_value.append(number)
            else:
                pass

        #Find length of neg_values:
        neg_length = len(neg_value)
        divisibility = neg_length % 2
        if divisibility == 0:
             pass
        else:
            diff_sum = diff_sum * -1

        print(diff_sum)
        diff_mean = diff_sum / self.n

        return diff_mean, diff_list

    def side_b(self):
        diff_mean, diff_list = self.side_a()

        squared_diff_list = []
        for number in diff_list:
            squared = number ** 2
            squared_diff_list.append(squared)


        squared_sum = sum(squared_diff_list)

        squared_mean = squared_sum / self.n
        
        #Final calculation

        L2_Scale_Loss = squared_mean - (diff_mean ** 2) / 2 
        print(L2_Scale_Loss)
        return L2_Scale_Loss


if __name__ == "__main__":
    ground_truth = [600, 300, 450]
    predictions = [500, 350, 400]

    L2_Scale_Invariant(ground_truth, predictions).side_b()