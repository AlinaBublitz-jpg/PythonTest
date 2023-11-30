import numpy as np
from sklearn.metrics import mean_squared_error
from data_handler import DataHandler


class DataAnalyzer(DataHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.best_fits = {}
        self.min_mse = np.inf

    def find_best_fit(self, train_table='train', ideal_table='ideal'):
        train_data = self.get_data_from_db(f'SELECT * FROM {train_table}')
        ideal_data = self.get_data_from_db(f'SELECT * FROM {ideal_table}')

        for x in train_data['x'].unique():
            self.best_fits[x] = []
            train_data_x = train_data[train_data['x'] == x]

            for i in range(1, 5):
               best_fit = None
               self.min_mse = np.inf

               for j in range(1, 51):
                    mse = mean_squared_error(train_data_x[f'y{i}'], ideal_data[ideal_data['x'] == x][f'y{j}'])
                    if mse < self.min_mse:
                        self.min_mse = mse
                        best_fit = j
            self.best_fits[x].append(best_fit)
        test_data = self.get_data_from_db(f'SELECT * FROM {test_table}')

        for best_fit in self.best_fits:
            ideal_data = self.get_data_from_db(f'SELECT y{best_fit} FROM ideal')
            mse = mean_squared_error(test_data['y1'], ideal_data[f'y{best_fit}'])
            if mse > np.sqrt(2) * self.min_mse:
                print(f'Test dataset does not match the ideal function {best_fit}.')

    def save_deviation(self, test_table='test'):
        test_data = self.get_data_from_db(f'SELECT * FROM {test_table}')
        for best_fit in self.best_fits:
            ideal_data = self.get_data_from_db(f'SELECT y{best_fit} FROM ideal')
            deviation = test_data['y1'] - ideal_data[f'y{best_fit}']
            self.get_data_from_db(f'UPDATE {test_table} SET delta_y = {deviation} WHERE ideal_func = "Funk{best_fit}"')

            # For each x pos 

