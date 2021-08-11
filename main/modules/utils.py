import logging
import os
import datetime

log_storage_relative_path = '../data/logs/'
loggers = {}


def create_logger(name='defaultname', level='info', path_to_logs=log_storage_relative_path):
    if name in loggers:
        return loggers.get(name)

    logger = logging.getLogger(name)
    level = {
        'critical': logging.CRITICAL,
        'error': logging.ERROR,
        'warning': logging.WARNING,
        'info': logging.INFO,
        'debug': logging.DEBUG,
    }.get(level.lower())
    logger.setLevel(level)

    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
    file_handler = logging.FileHandler(f'{path_to_logs}{datetime.date.today()}.log')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)
    logger.addHandler(file_handler)
    loggers[name] = logger
    return logger


def clean_old_logs(path_to_logs=log_storage_relative_path):
    for file in os.listdir(log_storage_relative_path):
        if file.endswith('.log'):
            pass
            # TODO finish this
