import yaml
import os
from utils.logger import log


def config(config_path="config.yaml"):
    abs_path = os.path.abspath(config_path)

    log.info(f"Using config path: {abs_path}")

    if not os.path.exists(abs_path):
        raise FileNotFoundError(f"Config file not found: {abs_path}")

    with open(abs_path, 'r') as f:
        config_data = yaml.safe_load(f)

    if not config_data:
        raise ValueError("Config file is empty or invalid")

    return config_data