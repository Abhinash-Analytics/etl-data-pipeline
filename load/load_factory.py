from .write_csv import WriteCSV
from .write_db import WriteDB
from .write_json import WriteJSON
from utils.config_loader import log

class LoadFactory:

    @staticmethod
    def get_loader(config):
        output_type = config['type']
        log.info(f"the output type is: {output_type}")

        if output_type == 'csv':
            return WriteCSV(config['output_path'])
        elif output_type == 'db':
            return WriteDB(config)
        elif output_type == 'json':
            return WriteJSON(config['output_path'])
        else:
            raise ValueError(f"unsupported output type: {output_type}")