from sqlalchemy import create_engine
from utils.logger import log

class WriteDB:
    def __init__(self, db_config):
        self.db_name = db_config['db_name']
        self.user_name = db_config['user_name']
        self.password = db_config['password']
        self.host = db_config['host']
        self.port = db_config['port']
        self.table = db_config['table']
    
    def write(self, df):
        log.info(f"Writing data to DB table: {self.table}")

        engine = create_engine(
            f"postgresql://{self.user_name}:{self.password}@{self.host}:{self.port}/{self.db_name}"
        )

        df.to_sql(
            self.table,
            engine,
            if_exists = 'replace',
            index = False
        )

        log.info(f"Successfully wrote {len(df)} records to DB")