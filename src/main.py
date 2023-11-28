from sqlalchemy import Float, Text
from data_handler import DataHandler

# Initialize data handler
db_handler = DataHandler()

# Define training table
table_training = {'x': Float}
table_training.update({f'y{i}': Float for i in range(1, 5)})

# Define test table
table_test = {
    'x': Float,
    'y1': Float,
    'delta_y': Float,
    'ideal_func': Text
}

# Define ideal table
table_ideal = {'x': Float}
table_ideal.update({f'y{i}': Float for i in range(1, 51)})


# Create tables
db_handler.create_table('test', table_test)
db_handler.create_table('train', table_training)
db_handler.create_table('ideal', table_ideal)


# Load data to tables
db_handler.load_csv_to_db('data/test.csv', 'test')
db_handler.load_csv_to_db('data/train.csv', 'train')
db_handler.load_csv_to_db('data/ideal.csv', 'ideal')




output = db_handler.get_data_from_db('SELECT * FROM test')

print(output)

