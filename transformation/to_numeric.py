import pandas as pd
from .base import Correction
from utils.logger import log

class ToNumeric(Correction):
    def __init__(self, columns):
        self.columns = columns

    def apply(self, df):
        log.info(f"Converting to numeric: {self.columns}")

        # log.info(f"the data set before to numeric: {df.columns.to_list()}")
        for col in self.columns:
            # log.info(f"the column to convert to numeric: {col}")
            df[col] = pd.to_numeric(df[col], errors = 'coerce')

        return df