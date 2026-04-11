import pandas as pd
from sqlalchemy import create_engine
from .base import DataSource
from utils.logger import log

class DatabaseSource(DataSource):

    def __init__(self, db_name, user_name, password, host, port, query):
        self.db_name = db_name
        self.user_name = user_name
        self.password = password
        self.host = host
        self.port = port
        self.query = query

    def read(self):
        log.info("Reading from Database")

        engine = create_engine(
            f"postgresql://{self.user_name}:{self.password}@{self.host}:{self.port}/{self.db_name}"
        )

        df = pd.read_sql(self.query, engine)
        
        log.info(f"The length of the df in sql is: {len(df)}")
        return df