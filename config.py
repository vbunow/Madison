import pytest
import driver
from selenium.webdriver import Firefox
from selenium import webdriver

lesson = 0


@pytest.fixture()
def webdriver(request):
	driver.browser = Firefox()
	request.addfinalizer(driver.browser.quit)
	#return driver.browser

'''browser = None
timeout = 4'''
