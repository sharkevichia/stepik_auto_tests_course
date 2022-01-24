from selenium import webdriver
import time
import unittest


class test_reg_page(unittest.TestCase):
	def test_registration_page_1(self):
		link = "http://suninjuly.github.io/registration1.html"
		browser = webdriver.Chrome()
		browser.get(link)
		input1 = browser.find_element_by_xpath("//input[@class='form-control first' and @required]")
		input1.send_keys("req1")
		input2 = browser.find_element_by_xpath("//input[@class='form-control second' and @required]")
		input2.send_keys("req2")
		input3 = browser.find_element_by_xpath("//input[@class='form-control third' and @required]")
		input3.send_keys("req3")
		time.sleep(5)
		button = browser.find_element_by_css_selector("button.btn")
		button.click()
		time.sleep(5)
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		welcome_text = welcome_text_elt.text
		self.assertEqual("(страница 1)", welcome_text,"")
	def test_registration_page_2(self):
		link = "http://suninjuly.github.io/registration2.html"
		browser = webdriver.Chrome()
		browser.get(link)
		input1 = browser.find_element_by_xpath("//input[@class='form-control first' and @required]")
		input1.send_keys("req1")
		input2 = browser.find_element_by_xpath("//input[@class='form-control second' and @required]")
		input2.send_keys("req2")
		input3 = browser.find_element_by_xpath("//input[@class='form-control third' and @required]")
		input3.send_keys("req3")
		button = browser.find_element_by_css_selector("button.btn")
		time.sleep(5)
		button.click()
		time.sleep(5)
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		welcome_text = welcome_text_elt.text
		self.assertEqual("(страница 2)", welcome_text,"")
if __name__ == '__main__':
	unittest.main()

