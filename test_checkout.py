from selenium.webdriver import Firefox
from webium.wait import wait
import pytest
from madison import *
from config import *
from allure.constants import AttachmentType
import allure

email = "miha@cvbiop.ua" 
passw = "miha12"


def test_checkout(webdriver):
	lesson = 0
	url = "http://brainacad.demo.site/"
	if lesson != 0:
		url = url + 'lesson_' + str(lesson)	
	#Open site http://brainacad.demo.site/
	visit(url)
	page = MadisonPage(driver = driver.browser)
	wait(lambda: page.is_element_present('account'))

	#Go to ACCOUNT -> Login
	page.account.click()
	page.log_in.click()
	page = LoginPage(driver = driver.browser)
	wait(lambda: page.is_element_present('log_btn'))

	#Enter email, password and submit
	page.login(email, passw)

	#Go to ACCESSORIES -> Eyewear
	page.go_to_menuitem(driver.browser,2,12)
	page = GoodsList(driver = driver.browser)

	#Add 1 item to cart
	product = page.items[0].link.text
	page.items[0].add_to_cart.click()
	page = ShoppingCart(driver = driver.browser)

	#Go to checkout
	page.checkout[0].click()
	page.continu1.click()
	page.free.click()
	page.continu2.click()
	page.continu3.click()
	page.terms_agree.click()
	page.place_order.click()

	allure.attach("Results", driver.browser.page_source, AttachmentType.HTML)
	#Order verification
	page.order.click()	
	assert product == page.product_name.text
		

if __name__ == '__main__':
	driver.browser = Firefox()
	test_checkout(driver.browser)
	