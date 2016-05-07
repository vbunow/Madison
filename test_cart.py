from selenium.webdriver import Firefox
from webium.wait import wait
from madison import *
import pytest
from config import *
from allure.constants import AttachmentType
import allure

email = "miha@ttwrxtt.ua" 
passw = "miha12" 


def test_add_to_cart1(webdriver):
	#Lesson choose
	url = "http://brainacad.demo.site/"
	lesson = 1
	if lesson != 0:
		url = url + 'lesson_' + str(lesson)	

	#Open site http://brainacad.demo.site/
	visit(url)
	page = MadisonPage(driver = driver.browser)
	wait(lambda: page.is_element_present('account'))

	#Go to ACCESSORIES -> Jewerly
	page.go_to_menuitem(driver.browser,2,12)
	page = GoodsList(driver = driver.browser)

	#Add to cart 1 item 1 qty
	page.items[0].add_to_cart.click()

	page = ShoppingCart(driver = driver.browser)
	price = float(page.items[0].price.text[1:])
	qty = int(page.items[0].qty.get_attribute('value'))
	subtotal = float(page.items[0].subtotal.text[1:])
	allure.attach("Results", driver.browser.page_source, AttachmentType.HTML)
	assert subtotal == price * qty, "Subtotal price wrong"

def test_add_to_cart2(webdriver):		
	#Lesson choose
	url = "http://brainacad.demo.site/"
	lesson = 1
	if lesson != 0:
		url = url + 'lesson_' + str(lesson)	

	#Open site http://brainacad.demo.site/
	visit(url)
	page = MadisonPage(driver = driver.browser)
	wait(lambda: page.is_element_present('account'))

	#Go to ACCESSORIES -> Jewerly
	page.go_to_menuitem(driver.browser,2,13)
	page = GoodsList(driver = driver.browser)

	#Open product details
	page.items[0].link.click()
	page = ProductDetals(driver = driver.browser)

	#Add to cart 1 item 5 qty
	set_value(page.qty, '5')
	page.add_button.click()

	page = ShoppingCart(driver = driver.browser)
	qty = int(page.items[0].qty.get_attribute('value'))
	allure.attach("Results", driver.browser.page_source, AttachmentType.HTML)
	assert qty == 5, "Items Qty Wrong"




if __name__ == '__main__':
	driver.browser = Firefox()
	test_add_to_cart2(driver.browser)
	