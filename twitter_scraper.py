#LoginTwitter, selenium is good to be used for scraping dynamic website
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

#for sleeping when accessing the website
from time import sleep
import random

#For file saving
import os
import csv



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
		self.filepath = "./outputs"
		self.filename = None
	def searchByUser(self, searchUsername): #can be run without logging in
		self.searchUsername = searchUsername
		#https://twitter.com/CDCgov
		self.url = f"https://twitter.com/{searchUsername}"
		try:
			# WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(self.url))
			sleep(random.uniform(1, 2))
			self.driver.get(self.url)
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
		self.getAllPostsByUser()
	def getAllPostsByUser(self):
		self.saveToCsv(None, 'w')  # create file for saving records
		end_of_scroll_region = False
		unique_tweets = set()
		last_position = None
		while not end_of_scroll_region:
			cards = self.collectTweetsCurrentView()
			for card in cards:
				try:
					tweet = self.getDataCurrentCard(card)
				except exceptions.StaleElementReferenceException:
					continue
				if not tweet:
					continue
				tweet_id = self.generateTweetId(tweet)
				if tweet_id not in unique_tweets:
					unique_tweets.add(tweet_id)
					print(tweet)
					self.saveToCsv(tweet)
			last_position, end_of_scroll_region = self.scrollDownPage( last_position)
	def saveToCsv(self, data, mode='a+'):
		if not os.path.exists(self.filepath):
			print(self.filepath)
			os.mkdir(self.filepath)
		filename = f"{self.filepath}/{self.searchUsername}_posts_data.csv"
		header = ['User', 'Handle', 'PostDate', 'TweetText', 'ReplyCount', 'RetweetCount', 'LikeCount']
		with open(filename, mode=mode, newline='', encoding='utf-8') as f:
			writer = csv.writer(f)
			if mode == 'w':
				writer.writerow(header)
			if data:
				writer.writerow(data)
		self.filename = filename
	def getFilename(self):
		return self.filename
	def generateTweetId(self, tweet):
		return ''.join(tweet)
	def scrollDownPage(self, last_position, num_seconds_to_load=0.5, scroll_attempt=0, max_attempts=5):
		end_of_scroll_region = False
		self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		sleep(num_seconds_to_load)
		curr_position = self.driver.execute_script("return window.pageYOffset;")
		if curr_position == last_position:
			if scroll_attempt < max_attempts:
				end_of_scroll_region = True
			else:
				self.drive = last_position
				self.scrollDownPage(curr_position, scroll_attempt + 1)
		last_position = curr_position
		return last_position, end_of_scroll_region
	def collectTweetsCurrentView(self, lookback_limit=25):
		page_cards = self.driver.find_elements_by_xpath('//div[@data-testid="tweet"]')
		if(len(page_cards) <= lookback_limit):
			return page_cards
		else:
			return page_cards[-lookback_limit:]
	def getDataCurrentCard(self, card):
		try:
			user = card.find_element_by_xpath('.//span').text
		except exceptions.NoSuchElementException:
			user = ""
		except exceptions.StaleElementReferenceException:
			return
		try:
			handle = card.find_element_by_xpath('.//span[contains(text(), "@")]').text
		except exceptions.NoSuchElementException:
			handle = ""
		try:
			postdate = card.find_element_by_xpath('.//time').get_attribute('datetime')
		except exceptions.NoSuchElementException:
			return
		try:
			_comment = card.find_element_by_xpath('.//div[2]/div[2]/div[1]').text
		except exceptions.NoSuchElementException:
			_comment = ""
		try:
			_responding = card.find_element_by_xpath('.//div[2]/div[2]/div[2]').text
		except exceptions.NoSuchElementException:
			_responding = ""
		tweet_text = _comment + _responding
		try:
			reply_count = card.find_element_by_xpath('.//div[@data-testid="reply"]').text
		except exceptions.NoSuchElementException:
			reply_count = ""
		try:
			retweet_count = card.find_element_by_xpath('.//div[@data-testid="retweet"]').text
		except exceptions.NoSuchElementException:
			retweet_count = ""
		try:
			like_count = card.find_element_by_xpath('.//div[@data-testid="like"]').text
		except exceptions.NoSuchElementException:
			like_count = ""
		tweet = (user, handle, postdate, tweet_text, reply_count, retweet_count, like_count)
		return tweet
	def close(self):
		self.driver.quit()
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





