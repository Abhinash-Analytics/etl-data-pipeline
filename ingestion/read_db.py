import pandas as pd
import sqlite3
from .base import DataSource
from utils.logger import log

class DatabaseSource(DataSource):

    def __init__(self, db_path, query):
        self.db_path = db_path
        self.query = query

    def read(self):
        log.info("Reading from Database")

        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql(self.query, conn)
        conn.close()

        return df