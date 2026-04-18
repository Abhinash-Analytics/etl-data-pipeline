from ingestion.read_csv import ReadCSV
from ingestion.read_db import DatabaseSource
from .read_json import ReadJson

class SourceFactory:

    @staticmethod
    def get_source(config):

        #source = config['data_source']

        source_type = config['type']

       # print(f"password: {config['password']}")
        if source_type == 'csv':
            return ReadCSV(config['input_path'])
        elif source_type == 'db':
            return DatabaseSource(config)
        elif source_type == 'json':
            return ReadJson(config['input_path'])
        else:
            raise ValueError(f"Unknown source type: {source_type}")