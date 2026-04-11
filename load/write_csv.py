import os
from utils.logger import log

class WriteCSV:

    def __init__ (self, path):
        self.path = path

    def write(self, df):

        log.info(f"Start writing data into the csv: {self.path}")

        #create a folder if not exist
        os.makedirs(os.path.dirname(self.path), exist_ok = True)\
        
        #write into the path
        df.to_csv(self.path, index=False)

        log.info(f"succesfully written the csv data into {self.path}")