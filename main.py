from ingestion.read_csv import ReadCSV
from transformation.cleaning import *
from transformation.cleaning import Encoding
from utils.validation import Validation
from pipeline.pipeline import Pipeline
from utils.config_loader import config

_config = config();

pipeline = Pipeline(
    source=ReadCSV(_config['data_source']['input_path']),
    changes=[
        HandleIntegerMissingValues('TotalCharges'),
        DropNull(),
        DropColumn('customerID'),
        Encoding()
    ],
    validator=Validation(
        _config['validation']['rules'],
        _config['validation']['threshold'],
        _config['output']['dropped_records']
    )
)

if __name__ == "__main__":
    pipeline.run()