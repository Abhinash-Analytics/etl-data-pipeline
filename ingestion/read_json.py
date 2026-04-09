import pandas as pd
from .base import DataSource
from utils.logger import log

class JSONSource(DataSource):

    def __init__(self, path):
        self.path = path

    def read(self):
        log.info(f"Reading JSON File: {self.path}")
        return pd.read_json(self.path)