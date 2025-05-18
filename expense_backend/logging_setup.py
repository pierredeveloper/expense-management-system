import logging


def setup_logger(name, log_file='server.log', level=logging.DEBUG):
#def setup_logger(name):
    logger = logging.getLogger(name)

    # Configure the custom logger
    logger.setLevel(level)
    file_handler = logging.FileHandler(log_file)
    formatter = logging.FileHandler('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger



# def setup_logger(name):
#     logger = logging.getLogger(name)
#
#     # Configure the custom logger
#     logger.setLevel(logging.DEBUG)
#     file_handler = logging.FileHandler('server.log')
#     formatter = logging.FileHandler('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     file_handler.setFormatter(formatter)
#     logger.addHandler(file_handler)
#
#     return logger




