import os
from utils.logger import log


class WriteJSON:

    def __init__(self, path):
        self.path = path

    def write(self, df):
        log.info(f"Writing output to JSON: {self.path}")

        # Create folder if not exists
        os.makedirs(os.path.dirname(self.path), exist_ok=True)

        df.to_json(
            self.path,
            orient='records',   # 🔥 best for APIs / downstream
            indent=4
        )

        log.info(f"Successfully wrote {len(df)} records to JSON")