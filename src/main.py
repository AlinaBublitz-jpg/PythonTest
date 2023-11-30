from data_handler import DataHandler
from schema.index import table_training, table_test, table_ideal

# Initialize data handler
db_handler = DataHandler()


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

