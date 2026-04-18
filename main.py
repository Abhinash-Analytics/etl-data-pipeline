from ingestion.read_csv import ReadCSV
from transformation.cleaning import *
from transformation.cleaning import Encoding
from utils.validation import Validation
from pipeline.pipeline import Pipeline
from utils.config_loader import config
from ingestion.source_factory import SourceFactory
from transformation.transformation_factory import TransformationFactory
from load.load_factory import LoadFactory

def main():
    _config = config();

    for source_config in _config['data_source']:
        log.info(f"initiating source_config :{source_config}")

        source = SourceFactory.get_source(source_config)

        transformations = TransformationFactory.build(_config['changes'], _config)

        validator=Validation(
                _config['validation']['rules'],
                _config['validation']['threshold'],
                _config['dropped_records']
            )

        # Load (Write output)
        loader = LoadFactory.get_loader(source_config)

        pipeline = Pipeline(
            source = source,
            changes = transformations,
            validator = validator,
            loader = loader
        )

        # Run pipeline
        pipeline.run()

if __name__ == "__main__":
    main()