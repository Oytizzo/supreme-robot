from .pytest_log_func import log_to_file
import pytest


# To use this decorator, simply apply it to the function that you want to log to a file, like so:
@log_to_file("test.log")
def test_something():
    assert 1 == 1

# When you run your pytest tests, you should see log messages that indicate when the function starts
# and finishes in the specified log file. Note that you'll need to configure the logging system appropriately
# to see the log messages in your output.
