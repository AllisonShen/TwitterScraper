#LoginTwitter
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.common import exceptions
# from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome

#For typing the password secretly
from easygui import passwordbox # work for both
import getpass #error message at IDE, only work at terminal
import pyinputplus as pyip # error message at IDE, only work at terminal

from time import sleep
import random

#twitter scraper object
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
		#https://twitter.com/CDCgov
		self.url = f"https://twitter.com/{searchUsername}"
		try:
			# WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(self.url))
			sleep(random.uniform(1, 2))
			self.driver.get('https://twitter.com/' + searchUsername)
			sleep(random.uniform(1, 2))

			try:
				followOthers = self.driver.find_element_by_xpath('//a[contains(@href,"/following")]/span[1]/span[1]').text
				followers = self.driver.find_element_by_xpath('//a[contains(@href,"/followers")]/span[1]/span[1]').text
			except exceptions.NoSuchElementException as e:
				followOthers = None
				followers = None
				print(e)
				return False
			try:
				element = self.driver.find_element_by_xpath('//div[contains(@data-testid,"UserProfileHeader_Items")]//a[1]')
				website = element.get_attribute("href")
			except Exception as e:
				website = ""
				print(e)
			try:
				description = self.driver.find_element_by_xpath('//div[contains(@data-testid,"UserDescription")]').text
			except exceptions.NoSuchElementException as e:
				description = ""
				print(e)
			print(f"---------------  {searchUsername} information : ---------------")
			print("Following : ", followOthers)
			print("Followers : ", followers)
			print("Description : ", description)
		except exceptions.TimeoutException:
			print("Time out")
			return False
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
			return False
		try:
			# self.password = pyip.inputPassword("Enter your password: ") #method one
			# self.password = getpass.getpass("Enter your password: ") #method two
			self.password = passwordbox("What is your password ?") #method three
			pwd_input = self.driver.find_element_by_xpath('//input[@name="session[password]"]')
			pwd_input.send_keys(self.password)
		except ValueError:
			print("Please type in a valid password")
			return False
		try:
			pwd_input.send_keys(Keys.RETURN)
			self.url = "https://twitter.com/home"
			WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(self.url))
		except exceptions.TimeoutException:
			print("Timeout during waiting for home screen")
			return False





