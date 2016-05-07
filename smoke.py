'''page.account.click()
		page.log_in.click()
		page = LoginPage(driver = driver.browser)
		wait(lambda: page.is_element_present('log_btn'))
		page.login(email, passw)'''


	'''def test_2(webdriver):
	#Lesson choose
	lesson = 0
	url = "http://brainacad.demo.site/"
	if lesson != 0:
		url = url + 'lesson_' + str(lesson)	

	#Open site http://brainacad.demo.site/
	visit(url)
	page = MadisonPage(driver = driver.browser)
	wait(lambda: page.is_element_present('account'))

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

	#Order verification
	page.order.click()
	assert product == page.product_name.text'''