# from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from selenium.common import exceptions
from selenium.webdriver import Chrome
import getpass

import pyinputplus as pyip

class LoginTwitter(object):
    def __init__(self, linkLogin, username):  #'https://twitter.com/login', 'xiaxin.shen@outlook.com'
        self.url = linkLogin
        self.username = username
        self.password = None
        self.driver = None
    def login(self):
        try:
            self.driver = Chrome()
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
            return False
        return True




