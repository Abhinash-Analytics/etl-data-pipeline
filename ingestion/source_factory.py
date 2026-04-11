from ingestion.read_csv import ReadCSV


class SourceFactory:

    @staticmethod
    def get_source(config):

        #source = config['data_source']

        source_type = config['type']

        if source_type == 'csv':
            return ReadCSV(config['input_path'])

        else:
            raise ValueError(f"Unknown source type: {source_type}")