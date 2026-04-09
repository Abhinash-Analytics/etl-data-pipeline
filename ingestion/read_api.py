import pandas as pd
import requests
from .base import DataSource
from utils.logger import log

class APISource(DataSource):

    def __init__(self, url):
        self.url = url

    def read(self):
        log.info(f"Calling API: {self.url}")

        response = requests.get(self.url)
        response.raise_for_status()

        return pd.DataFrame(response.json())