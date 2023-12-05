import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
def test_navigation_and_form_submission(browser):
    # Navigate to root URL
    browser.get('http://localhost:5000')

    # Check if we are on the correct page
    assert 'Welcome' in browser.title
