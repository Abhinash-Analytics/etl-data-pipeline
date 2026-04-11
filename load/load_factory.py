from .write_csv import WriteCSV

class LoadFactory:

    @staticmethod
    def get_loader(config):
        output_type = config['output']['type']

        if output_type == 'csv':
            return WriteCSV(config['output']['path'])
        
        else:
            raise ValueError(f"unsupported output type: {output_type}")