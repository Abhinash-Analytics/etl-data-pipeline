from .write_csv import WriteCSV
from .write_db import WriteDB
from .write_json import WriteJSON

class LoadFactory:

    @staticmethod
    def get_loader(config):
        output_type = config['output']['type']

        if output_type == 'csv':
            return WriteCSV(config['output']['path'])
        elif output_type == 'db':
            return WriteDB(config['output']['database'])
        elif output_type == 'json':
            return WriteJSON(config['output']['path'])
        else:
            raise ValueError(f"unsupported output type: {output_type}")