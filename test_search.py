from selenium.webdriver import Firefox
from webium.wait import wait
from madison import *
import pytest
from config import *
from allure.constants import AttachmentType
import allure


def test_search(webdriver):
	#Lesson choose
	url = "http://brainacad.demo.site/"
	lesson = 0
	if lesson != 0:
		url = url + 'lesson_' + str(lesson)	

	# Search text
	text = "pants"

	#Open site http://brainacad.demo.site/
	visit(url)
	page = MadisonPage(driver = driver.browser)
	wait(lambda: page.is_element_present('search'))

	#Enter search text
	set_value(page.search, text)
	page.search.submit()

	#Search results 
	page = GoodsList(driver = driver.browser)
	allure.attach("Results", driver.browser.page_source, AttachmentType.HTML)
	assert text == page.search.get_attribute('value'), "Wrong text search"
	assert len(page.items) > 0, "Number of Result items should be > 0"


if __name__ == '__main__':
	driver.browser = Firefox()
	test_search(driver.browser)