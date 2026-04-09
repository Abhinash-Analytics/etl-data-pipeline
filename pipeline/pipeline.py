import logging as log
from utils.config_loader import config

_config = config();

class Pipeline:
    def __init__(self, source, changes, validator):
        self.source = source
        self.changes = changes
        self.validator = validator

    def run(self):
        log.info("Pipeline started")

        df = self.source.read()

        for step in self.changes:
            df = step.apply(df)

        df = self.validator.clean(df)

        df.to_csv(_config['output']['processed_data'], index=False)

        log.info("Pipeline completed successfully")