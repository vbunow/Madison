from webium import BasePage, Find, Finds
from webium.controls.link import Link
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import driver
import allure


class MadisonPage(BasePage):
	account = Find(by = By.XPATH, value = ".//*[@id='header']//span[text()='Account']")
	register = Find(by = By.XPATH, value = ".//*[@id='header-account']//li[5]/a")
	log_in = Find(by = By.XPATH, value = ".//*[@id='header-account']//li[6]/a")
	search = Find(by = By.ID, value = "search")
	newsletter = Find(by = By.ID, value = "newsletter")
	subscribe = Find(by = By.XPATH, value = ".//button[@title='Subscribe']")
	success_msg = Find(by = By.CLASS_NAME, value = "success-msg")
	error_msg = Find(by = By.CSS_SELECTOR, value = ".error-msg")

	continu1 = Find(by = By.XPATH, value = ".//*[@id='billing-buttons-container']/button")
	continu2 = Find(by = By.XPATH, value = ".//*[@id='shipping-method-buttons-container']/button")
	continu3 = Find(by = By.XPATH, value = ".//*[@id='payment-buttons-container']/button")
	free = Find(by = By.XPATH, value = ".//*[@id='s_method_freeshipping_freeshipping']")
	xpd = Find(by = By.XPATH, value = ".//*[@id='s_method_ups_XPD']")
	terms_agree = Find(by = By.XPATH, value = ".//*[@id='agreement-1']")
	place_order = Find(by = By.XPATH, value = ".//*[@id='review-buttons-container']/button")
	order = Find(by = By.CSS_SELECTOR, value = ".col-main>p>a")
	product_name = Find(by = By.CSS_SELECTOR, value = ".product-name")
	
	menu = Finds(Link, By.CSS_SELECTOR, value = '.level0>a')
	menuitem = Finds(Link, By.CSS_SELECTOR, value = '.level1>a')

	@allure.step('Go to Menu -> Item')
	def go_to_menuitem(self, webdriver, m, i):
		actions = ActionChains(webdriver)
		actions.move_to_element(self.menu[m])
		actions.click(self.menuitem[i])
		actions.perform()
	 

class PrudutItem(WebElement):
	link = Find(Link, By.XPATH, './h2/a')
	price = Find(by = By.XPATH, value = ".//span[@class='price']")
	add_to_wish = Find(by = By.XPATH, value = ".//a[@class='link-wishlist']")
	add_to_cart = Find(by = By.XPATH, value = ".//button")

class GoodsList(MadisonPage):
	sort_by = Find(by = By.XPATH, value = ".//*[@id='top']//select[@title='Sort By']")
	items = Finds(PrudutItem, By.XPATH, value = ".//div[@class='product-info']")

class ProductDetals(MadisonPage):
	color = Find(by = By.XPATH, value = ".//*[@id='attribute92']")
	size = Find(by = By.XPATH, value = ".//*[@id='attribute180']>")
	qty = Find(by = By.XPATH, value = ".//*[@id='qty']")	
	add_button = Find(by = By.CSS_SELECTOR, value = ".button.btn-cart")





class RegistrationPage(MadisonPage):
	firstname = Find(by = By.ID, value = "firstname")
	lastname = Find(by = By.ID, value = "lastname")
	email_address = Find(by = By.ID, value = "email_address")
	password = Find(by = By.ID, value = "password")
	confirm = Find(by = By.ID, value = "confirmation")
	button_reg = Find(by = By.XPATH, value = ".//*[@id='form-validate']//button")
	
	
	@allure.step('Registration on site')
	def register(self, fname, lname, email, passw, confirm):
		set_value(self.firstname, fname)
		set_value(self.lastname, lname)
		set_value(self.email_address, email)
		set_value(self.password, passw)
		set_value(self.confirm, confirm)
		self.button_reg.click()


class LoginPage(MadisonPage):
	email = Find(by = By.ID, value = "email")
	passw = Find(by = By.ID, value = "pass")
	log_btn = Find(by = By.ID, value = "send2")
	welcom_msg = Find(by = By.CSS_SELECTOR, value = ".hello>strong")

	@allure.step('Login on site')
	def login(self, email, passw):
		self.email.clear()
		self.email.send_keys(email)
		self.passw.clear()
		self.passw.send_keys(passw)
		self.log_btn.click()

class CartItem(WebElement):
	name = Find(Link, By.XPATH, './/h2/a')
	price = Find(by = By.XPATH, value = "./td[3]//span[@class='price']")
	qty = Find(by = By.XPATH, value = "./td[4]//input")
	subtotal = Find(by = By.XPATH, value = "./td[5]//span[@class='price']")


class ShoppingCart(MadisonPage):
	items = Finds(CartItem, By.XPATH, value = ".//*[@id='shopping-cart-table']//tbody/tr")
	checkout = Finds(by = By.CSS_SELECTOR, value = ".button.btn-proceed-checkout.btn-checkout")

class AccountPage(MadisonPage):
	manage_addr =  Find(by = By.XPATH, value = ".//a[text()='Manage Addresses']")

class AddNewAddress(MadisonPage):
	country = Find(by = By.XPATH, value = ".//*[@id='country']")
	telephone = Find(by = By.XPATH, value = ".//*[@id='telephone']")
	street = Find(by = By.XPATH, value = ".//*[@id='street_1']")
	city = Find(by = By.XPATH, value = ".//*[@id='city']")
	index = Find(by = By.XPATH, value = ".//*[@id='zip']")
	save = Find(by = By.XPATH, value = ".//*[@id='form-validate']//button")


	@allure.step('Add new address')
	def add_address(self, country, telephone, street, city, index):
		Select(self.country).select_by_visible_text(country)
		set_value(self.telephone, telephone)
		set_value(self.street, street)
		set_value(self.city, city)
		set_value(self.index, index)
		self.save.click()



def set_value(element, value):
	element.clear()
	element.send_keys(value)

def visit(url):
    driver.browser.get(url)



