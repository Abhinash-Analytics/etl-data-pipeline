import pandas as pd
import numpy as np
from .base import Correction
from utils.logger import log
from utils.config_loader import config

_config = config()

class HandleIntegerMissingValues(Correction):
    def __init__(self, column, missing_values):
        self.column = column
        self.missing_values = missing_values

    def apply(self, df):
        log.info(f"hangling missing interger data: {self.column}")
                
        print ("------ Missing values: ", df[self.column])
        df[self.column] = df[self.column].replace(self.missing_values, np.nan)
        df[self.column] = pd.to_numeric(df[self.column], errors='coerce')

        return df

class DropNull(Correction):
    def apply(self, df):
        log.info('Dropping NAN values')
        df = df.dropna()

        print(f"Drop Null: {df.columns.tolist()}")
        return df
    
class DropColumn(Correction):
    def __init__(self, column):
        self.column = column

    def apply(self, df):
        log.info(f'Dropping column: {self.column}')
        if self.column in df.columns:
            df = df.drop(columns=[self.column])

        print(f"Drop Column: {df.columns.tolist()}")
        return df
    
class Encoding(Correction):
    def apply(self, df):
        log.info('apply encoding on objects')

        col_cat = df.select_dtypes(include = ['object', 'category']).columns

        # Avoid encoding numeric like columns
        col_cat = [col for col in col_cat if df[col].nunique() < 20]

        for col in col_cat:
            unique_val = df[col].nunique()

            if unique_val == 2:
                # log.info(f"Label encoding: {col}")
                df[col] = df[col].astype('category').cat.codes

            if unique_val > 2:
                # log.info(f"Hot encoding: {col}")
                df = pd.get_dummies(df, columns = [col])

                bool_cols = df.select_dtypes(include = 'bool').columns
                df[bool_cols] = df[bool_cols].astype(int)
        
        # for col in col_cat:
        #     print(f'{col}: ', df[col].unique())

        print(f"encoding: {df.columns.tolist()}")
        return df