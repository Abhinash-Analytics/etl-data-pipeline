import logging as log
from utils.config_loader import config

_config = config();
#print("----------logger config", _config)
print("----------logger----------")

log.basicConfig(
    level=log.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        log.FileHandler(_config['logging']['log_file']),
        log.StreamHandler()
    ],
    force=True
)