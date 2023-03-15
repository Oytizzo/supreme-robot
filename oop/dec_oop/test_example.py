from .log_decorators import class_logger, class_logger_to_file, func_log_to_file
import pytest


# To use this decorator, simply apply it to the function that you want to log to a file, like so:
@func_log_to_file("test.log")
def test_something():
    assert 1 == 0


@class_logger
class TestSomething:
    def test_one(self):
        assert 1 == 1

    def test_two(self):
        assert 2 == 2


@class_logger_to_file("test.log")
class TestSomething:
    def test_one(self):
        assert 1 == 1

    def test_two(self):
        assert 2 == 2
