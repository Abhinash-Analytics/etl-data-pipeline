import pandas as pd
from .base import DataSource
from utils.logger import log

class ReadCSV(DataSource):
    def __init__(self, path):
        self.path = path

    def read(self):
        log.info(f"Reading CSV file: {self.path}")
        return pd.read_csv(self.path)