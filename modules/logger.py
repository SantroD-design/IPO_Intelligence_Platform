import logging
import os
from config.settings import LOG_FOLDER

# Create logs folder if it doesn't exist
os.makedirs(LOG_FOLDER, exist_ok=True)

LOG_FILE = os.path.join(LOG_FOLDER, "ipo_platform.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)