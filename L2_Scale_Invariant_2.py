import math 


#apply logarithm log()
#calculate logarithmic difference
#square each logarithmic difference
#calculate the mean of the squared differences
#

class L2_Scale_Invariant():
    def __init__(self, ground_truth, predictions):
        self.ground_truth = ground_truth
        self.predictions = predictions

        self.n = len(self.ground_truth)

    def logarithm(self, number):
        logarithmic = math.log10(number)
        return logarithmic

    def log_diff(self, ground_truth_log, prediction_log):
        difference = ground_truth_log - prediction_log
        return difference

    def log_squared_diff(self, difference):
        squared_diff = difference ** 2
        return squared_diff

    def log_squared_mean(self, log_squared_differences):
        total_sum = sum(log_squared_differences)
        squared_mean = total_sum / self.n
        return squared_mean

    def log_mean(self, difference_list):
        total_sum = sum(difference_list)
        log_mean = total_sum / self.n
        return log_mean

    def term_1(self, squared_mean):
        total =  (1 / (2 * self.n)) * squared_mean
        return total

    def term_2(self, log_mean):
        total = (1 / (((2 * self.n) * log_mean) ** 2)) 
        return total

    def calculate(self):
        ground_log_numbers = []
        prediction_log_numbers = []
        for i in range(self.n):
            ground_log = self.logarithm(self.ground_truth[i])
            prediction_log = self.logarithm(self.predictions[i])
            ground_log_numbers.append(ground_log)
            prediction_log_numbers.append(prediction_log)

        difference_list = []
        for i in range(self.n):
            diff = self.log_diff(ground_log_numbers[i], prediction_log_numbers[i])
            difference_list.append(diff)

        log_squared_differences = []
        for i in range(self.n):
            squared_diff = self.log_squared_diff(difference_list[i])
            log_squared_differences.append(squared_diff)

        squared_mean = self.log_squared_mean(log_squared_differences)
        log_mean = self.log_mean(difference_list)

        term_1 = self.term_1(squared_mean)
        term_2 = self.term_2(log_mean)

        L2_Scale_Loss = term_1 - term_2
        print(L2_Scale_Loss)
        return L2_Scale_Loss

        
if __name__ == "__main__":
    ground_truth = [50, 100, 150]
    predictions = [45, 110, 140]
    L2_Scale_Invariant(ground_truth, predictions).calculate()
