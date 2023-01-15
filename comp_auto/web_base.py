import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


# Click web element
def click_item(data):
    """This function will click an item using the data any one will provide.
    data will be a tuple of two items(locator_attibute, attribute_value)"""
    # using that locator selector a functio will create a xpath, using what we will interect

    try:
        # driver = <selenium_driver>
        driver.click()
        print("Successfully clicked the element")
    except Exception as e:
        print(e)
