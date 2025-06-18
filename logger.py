# logger.py
import logging

# Create a logger for the entire project
logger = logging.getLogger("careerbot")
logger.setLevel(logging.INFO)  # Change to DEBUG for verbose logs

# Formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")

# Console Handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# File Handler (optional)
file_handler = logging.FileHandler("careerbot.log")
file_handler.setFormatter(formatter)

# Avoid duplicate logs
if not logger.hasHandlers():
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
