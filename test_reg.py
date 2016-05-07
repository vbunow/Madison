from selenium.webdriver import Firefox
from webium.wait import wait
from madison import *
import pytest
from config import *
from allure.constants import AttachmentType
import allure


fname = "Mihail"
lname = "Cherniavskiy" 
email = "miha@qweasd.ua" 
passw = "miha12" 

def test_registration1(webdriver):
	#Lesson choose
	url = "http://brainacad.demo.site/"
	lesson = 0
	if lesson != 0:
		url = url + 'lesson_' + str(lesson)	
	#Open site http://brainacad.demo.site/
	visit(url)
	page = MadisonPage(driver = driver.browser)
	wait(lambda: page.is_element_present('account'))
    
    #Choose ACCOUNT -> Register
	page.account.click()
	page.register.click()

    #Fill in Registration form
	page = RegistrationPage(driver = driver.browser)
	wait(lambda: page.is_element_present('button_reg'))

	#Submit
	page.register(fname, lname, email, passw, passw)
	allure.attach("Results", driver.browser.page_source, AttachmentType.HTML)
	assert page.is_element_present('success_msg')
	


if __name__ == '__main__':
	driver.browser = Firefox()
	test_reg1(driver.browser)

	

