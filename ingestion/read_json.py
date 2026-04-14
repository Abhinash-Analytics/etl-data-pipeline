import pandas as pd
import json
from .base import DataSource
from utils.logger import log

class ReadJson(DataSource):

    def __init__(self, path):
        self.path = path

    def read(self):
        log.info(f"Reading JSON File: {self.path}")
        
        with open(self.path) as f:
            data = json.load(f)

        df = pd.json_normalize(data)

        log.info(f"length of the record in read json: {df.head()}")

        return df