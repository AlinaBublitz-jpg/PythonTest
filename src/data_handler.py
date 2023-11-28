import pandas as pd
from sqlalchemy import Column, MetaData, Table, create_engine
import os

class DataHandler:
    def __init__(self, db_filename: str = 'database.db'):
        if not os.path.exists('runtime'):
            os.makedirs('runtime')
        self.engine = create_engine(f"sqlite:///runtime/{db_filename}")
        self.metadata = MetaData()

    def create_table(self, table_name: str, columns: dict):
        Table(
            table_name, 
            self.metadata, 
            *[Column(name, type_) for name, type_ in columns.items()]
        )
        self.metadata.create_all(self.engine)

    def load_csv_to_db(self, csv_path: str, table_name: str):
        df = pd.read_csv(csv_path)
        df.to_sql(table_name, self.engine, if_exists='replace', index=False)

    def get_data_from_db(self, query: str):
        return pd.read_sql_query(query, self.engine)