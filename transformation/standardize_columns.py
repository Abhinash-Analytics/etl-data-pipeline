import re
from .base import Correction
from utils.logger import log


class StandardizeColumns(Correction):

    def apply(self, df):
        log.info("Standardizing column names")

        def normalize(col):
            col = re.sub(r'(?<!^)(?=[A-Z])', '', col).lower()

            # Remove spaces
            col = col.replace(" ", "")

            return col

        df.columns = [normalize(col) for col in df.columns]

        log.info(f"Columns after standardization: {df.columns.tolist()}")

        return df