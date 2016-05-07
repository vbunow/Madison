from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from webium.wait import wait
import pytest
from madison import *
from config import *
from allure.constants import AttachmentType
import allure


fname = "Mihail"
lname = "Cherniavskiy" 
email = "miha@cvbiop.ua" 
passw = "miha12"

tel = "425023"
country = "Ukraine"
city = "Zaporozhye"
street = "Gudimenko 40, 100"
index = "69114"


def test_smoke(webdriver):
	#Lesson choose
	lesson = 0
	url = "http://brainacad.demo.site/"
	if lesson != 0:
		url = url + 'lesson_' + str(lesson)	

	#Open site http://brainacad.demo.site/
	visit(url)
	page = MadisonPage(driver = driver.browser)
	wait(lambda: page.is_element_present('account'))

	#Enter search text
	text = "pants"
	set_value(page.search, text)
	page.search.submit()

	#Search results 
	page = GoodsList(driver = driver.browser)
	assert text == page.search.get_attribute('value'), "Wrong text search"
	assert len(page.items) > 0, "Number of Result items should be > 0"

	#Choose ACCOUNT -> Register
	page.account.click()
	page.register.click()
	page = RegistrationPage(driver = driver.browser)

	#Fill in Registration form
	page.register(fname, lname, email, passw, passw)
	page = AccountPage(driver = driver.browser)

	#Manage Addreess click
	page.manage_addr.click()
	page = AddNewAddress(driver = driver.browser)

	#Fill in address
	page.add_address(country, tel, street, city, index)

	#Go to MEN -> Shirts
	page.go_to_menuitem(driver.browser, 1, 7)
	goods = GoodsList(driver = driver.browser)
	wait(lambda: goods.is_element_present('sort_by'), waiting_for = 'Wait for element SortBy')

	#Choose Select By Price
	Select(goods.sort_by).select_by_index(2)
	assert Select(goods.sort_by).first_selected_option.text == "Price"

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
	test_1(driver.browser)
