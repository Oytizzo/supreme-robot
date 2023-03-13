import logging
import pytest


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


# To use this decorator, simply apply it to the function that you want to log to a file, like so:
@log_to_file("test.log")
def test_something():
    assert 1 == 1


# When you run your pytest tests, you should see log messages that indicate when the function starts
# and finishes in the specified log file. Note that you'll need to configure the logging system appropriately
# to see the log messages in your output.
