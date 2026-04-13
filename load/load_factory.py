from .write_csv import WriteCSV
from .write_db import WriteDB

class LoadFactory:

    @staticmethod
    def get_loader(config):
        output_type = config['output']['type']

        if output_type == 'csv':
            return WriteCSV(config['output']['path'])
        elif output_type == 'db':
            return WriteDB(config['output']['database'])
        else:
            raise ValueError(f"unsupported output type: {output_type}")