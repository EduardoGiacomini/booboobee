import logging


class Logger:
    @staticmethod
    def setup(logger_level):
        line_format = '[%(asctime)s] | %(levelname)s]: %(message)s'
        date_format = '%d-%m-%Y %H:%M:%S'
        logging.basicConfig(format=line_format, datefmt=date_format, level=logger_level)
