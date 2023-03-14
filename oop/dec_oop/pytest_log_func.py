import logging


def log_to_file(logfile):
    def decorator(fn):
        logger = logging.getLogger(fn.__module__)
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        fh = logging.FileHandler(logfile)
        fh.setLevel(logging.INFO)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        def wrapper(*args, **kwargs):
            logger.info("Starting function: %s", fn.__name__)
            result = fn(*args, **kwargs)
            logger.info("Finished function: %s", fn.__name__)
            return result
        return wrapper

    return decorator
