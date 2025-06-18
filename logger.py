import logging
import os
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

load_dotenv()
# Get log_dir and log_filename from .env
LOG_DIR = os.getenv("LOG_DIR", "logs")
LOG_FILE_NAME = os.getenv("LOG_FILE", "careerbot.log")

# Make sure path is absolute and create folder if needed
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, LOG_DIR)
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, LOG_FILE_NAME)

# Configure logger
logger = logging.getLogger("careerbot")
logger.setLevel(logging.INFO)

# Create rotating file handler (max 5MB per file, keep 3 backups)
file_handler = RotatingFileHandler(LOG_FILE, maxBytes=5*1024*1024, backupCount=3)
file_handler.setLevel(logging.INFO)

# Create console handler (optional)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Log format
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
