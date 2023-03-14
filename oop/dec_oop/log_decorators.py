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


@class_logger_to_file("test.log")
class TestSomething:
    def test_one(self):
        assert 1 == 1

    def test_two(self):
        assert 2 == 2
