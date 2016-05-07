from selenium.webdriver import Firefox
from webium.wait import wait
from madison import *
import pytest
from config import *
from allure.constants import AttachmentType
import allure

def test_login1(webdriver):
	email = "miha@iop.ua" 
	passw = "miha12"  
	#Lesson choose
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
	allure.attach("Results", driver.browser.page_source, AttachmentType.HTML)
	assert page.is_element_present('welcom_msg')

def test_login2(webdriver):
	email = "miha@iop.ua" 
	passw = "111111"  
	#Lesson choose
	lesson = 6
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
	allure.attach("Results", driver.browser.page_source, AttachmentType.HTML)
	assert page.is_element_present('error_msg')
	
	


if __name__ == '__main__':
	driver.browser = Firefox()
	test_login2(driver.browser)
	