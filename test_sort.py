from selenium.webdriver import Firefox
from selenium.webdriver.support.select import Select
from webium.wait import wait
from madison import *
import pytest
from config import *
from allure.constants import AttachmentType
import allure


def test_sort_by_name(webdriver):
	#Lesson choose
	url = "http://brainacad.demo.site/"
	lesson = 0
	if lesson != 0:
		url = url + 'lesson_' + str(lesson)	

	#Open site http://brainacad.demo.site/
	visit(url)
	page = MadisonPage(driver = driver.browser)
	wait(lambda: page.is_element_present('account'))

	#Go to MEN -> Shirts
	page.go_to_menuitem(driver.browser, 1, 7)
	goods = GoodsList(driver = driver.browser)
	wait(lambda: goods.is_element_present('sort_by'), waiting_for = 'Wait for element SortBy')
    
    #Choose Select By Name
	Select(goods.sort_by).select_by_index(1)
	allure.attach("Results", driver.browser.page_source, AttachmentType.HTML)
	assert Select(goods.sort_by).first_selected_option.text == "Name"


def test_sort_by_price(webdriver):
	#Lesson choose
	url = "http://brainacad.demo.site/"
	lesson = 3
	if lesson != 0:
		url = url + 'lesson_' + str(lesson)	
	#Open site http://brainacad.demo.site/
	visit(url)
	page = MadisonPage(driver = driver.browser)
	wait(lambda: page.is_element_present('account'))

	#Go to MEN -> Shirts
	page.go_to_menuitem(driver.browser, 1, 7)
	goods = GoodsList(driver = driver.browser)
	wait(lambda: goods.is_element_present('sort_by'), waiting_for = 'Wait for element SortBy')

	#Choose Select By Price
	Select(goods.sort_by).select_by_index(2)
	allure.attach("Results", driver.browser.page_source, AttachmentType.HTML)
	assert Select(goods.sort_by).first_selected_option.text == "Price"
		

if __name__ == '__main__':
	driver.browser = Firefox()
	test_sort_by_price(driver.browser)

	