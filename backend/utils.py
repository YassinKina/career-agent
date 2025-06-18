import inspect
from logger import logger

def log_current_function():
    current_func = inspect.currentframe().f_back.f_code.co_name
    logger.info(f"Running function: {current_func}")
