import logging
import os
from datetime import datetime


def setup_logger(logger_name, log_level=logging.INFO):
    """
    Sets up a logger with the specified name and log level.

    Args:
        logger_name (str): Name of the logger
        log_level (int): Logging level (default: logging.INFO)

    Returns:
        logging.Logger: Configured logger instance
    """
    # Create logs directory if it doesn't exist
    log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs')
    os.makedirs(log_dir, exist_ok=True)

    # Create a logger
    logger = logging.getLogger(logger_name)

    # Only set up handlers if they don't exist
    if not logger.handlers:
        logger.setLevel(log_level)

        # Create file handler with rotating logs
        log_file = os.path.join(log_dir, f"{logger_name}_{datetime.now().strftime('%Y%m%d')}.log")
        file_handler = logging.FileHandler(log_file)

        # Create console handler
        console_handler = logging.StreamHandler()

        # Create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
