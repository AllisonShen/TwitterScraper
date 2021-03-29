#LoginTwitter
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.common import exceptions
from selenium.webdriver import Chrome
import getpass

# from selenium.common.exceptions import NoSuchElementException
import pyinputplus as pyip

#twitter scrapter object

class TwitterScraper(object):
	def __init__(self):
		#search by user
		self.searchUsername = None
		#login
		self.url = None
		self.username = None
		self.password = None
		self.driver = Chrome()
	def searchByUser(self, searchUsername):
		self.searchUsername = searchUsername
	def login(self, linkLogin, username):
		self.url = linkLogin
		self.username = username
		try:
			self.driver.get(self.url)
			xpath_username = '//input[@name="session[username_or_email]"]'
			WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, xpath_username)))
			uid_input = self.driver.find_element_by_xpath(xpath_username)
			uid_input.send_keys(self.username)
			print("Successfully fill in username")
		except exceptions.TimeoutException:
			print("Timeout for logging in")
		try:
			# self.password = pyip.inputPassword("Enter your password: ") #method one
			self.password = getpass.getpass("Enter your password: ") #method two
			pwd_input = self.driver.find_element_by_xpath('//input[@name="session[password]"]')
			pwd_input.send_keys(self.password)
		except ValueError:
			print("Please type in a valid password")
		try:
			pwd_input.send_keys(Keys.RETURN)
			url = "https://twitter.com/home"
			WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))
		except exceptions.TimeoutException:
			print("Timeout during waiting for home screen")





