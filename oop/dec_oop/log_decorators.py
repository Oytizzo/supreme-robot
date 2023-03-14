import logging
import pytest


def class_logger_to_file(logfile):
    def decorator(cls):
        logger = logging.getLogger(cls.__module__)
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        fh = logging.FileHandler(logfile)
        fh.setLevel(logging.INFO)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        for name, fn in cls.__dict__.items():
            if callable(fn) and name.startswith("test"):
                setattr(cls, name, _wrap_test_method(fn, logger))
        return cls

    return decorator


def _wrap_test_method(fn, logger):
    def wrapper(*args, **kwargs):
        logger.info("Starting test: %s", fn.__name__)
        result = fn(*args, **kwargs)
        logger.info("Finished test: %s", fn.__name__)
        return result
    return wrapper


def class_logger(cls):
    logger = logging.getLogger(cls.__module__)
    for name, fn in cls.__dict__.items():
        if callable(fn) and name.startswith("test"):
            setattr(cls, name, _wrap_test_method(fn, logger))
    return cls


def func_log_to_file(logfile):
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
