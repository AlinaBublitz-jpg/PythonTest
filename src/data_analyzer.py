import numpy as np
from sklearn.metrics import mean_squared_error
from data_handler import DataHandler


class DataAnalyzer(DataHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.best_fits = {}
        self.min_mse = np.inf

    def find_best_fit(train_set: np.array, ideal_set: np.array):
        y_train = train_set[:, 1]  # Extract y values

        best_curve = None
        lowest_mse = float('inf')

        for curve in ideal_set:
            if len(curve) != len(train_set):
                continue  # Skip this curve if it's not the same length as the train set

            y_curve = curve[:, 1]  # Extract y values

            # Compute the MSE between the y values of the curve and the training set
            mse = mean_squared_error(y_train, y_curve)

            if mse < lowest_mse:
                best_curve = curve
                lowest_mse = mse

        return best_curve, lowest_mse

    def save_deviation(self):
        return
        

