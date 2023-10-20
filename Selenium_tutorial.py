# The webdriver module is responsible for interacting with web browsers.
# It provides various classes and methods for creating browser instances and controlling them programmatically.
from selenium import webdriver
# The By class provides a set of locator strategies that you can use to locate HTML elements on a web page when
# using Selenium for web automation and testing.
from selenium.webdriver.common.by import By

# This line creates an instance of the Firefox web driver.
# It initializes a Firefox browser session that you can control through the driver variable.
driver = webdriver.Firefox()


# Navigate to root URL
# The default root URL of a flask application uses the host '127.0.0.1' and port '5000'.
driver.get('http://127.0.0.1:5000')

# Navigate to the search page
driver.get('http://localhost:5000/search')

# Navigate to the form page
driver.get('http://localhost:5000/form')

# locates an HTML element within a web page using the "name" attribute as a locator strategy.
element = driver.find_element(By.NAME, 'data')

element.send_keys('Selenium Test Data')  # Add text to the element

# Locate the button by its name
button = driver.find_element(By.NAME, 'button')

# Click the button
button.click()
# Wait for user input before closing the browser
input("Press Enter to close the browser...")
