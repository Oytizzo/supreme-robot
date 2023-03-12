import logging
import pytest


def log_test_class(cls):
    logger = logging.getLogger(cls.__module__)
    for name, fn in cls.__dict__.items():
        if callable(fn) and name.startswith("test"):
            setattr(cls, name, _wrap_test_method(fn, logger))
    return cls


def _wrap_test_method(fn, logger):
    def wrapper(*args, **kwargs):
        logger.info("Starting test: %s", fn.__name__)
        result = fn(*args, **kwargs)
        logger.info("Finished test: %s", fn.__name__)
        return result
    return wrapper


@log_test_class
class TestSomething:
    def test_one(self):
        assert 1 == 1

    def test_two(self):
        assert 2 == 2
