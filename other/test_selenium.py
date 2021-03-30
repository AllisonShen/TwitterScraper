#!/usr/bin/env python
# coding: utf-8

# In[7]:


from io import StringIO, BytesIO
import os
import re
from time import sleep
import random



import datetime
import pandas as pd
import platform

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# import pathlib

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from . import const
import urllib



# In[42]:


from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
from selenium.common import exceptions


# In[18]:


import getpass


# In[13]:


driver = Chrome()


# In[14]:


##################################login
url = 'https://twitter.com/login'
driver.get(url)


# In[15]:


xpath_username = '//input[@name="session[username_or_email]"]'

#input from the user # needs to be modified to the function's argument
username = "xiaxin.shen@outlook.com"
password = None
#input from the user

uid_input = driver.find_element_by_xpath(xpath_username)
uid_input.send_keys(username)

# single / means starts from the root
# double // means starts from current node & matches anywhere


# In[20]:


password = getpass.getpass() # make the input looks like a secret


# In[21]:


pwd_input = driver.find_element_by_xpath('//input[@name="session[password]"]')
pwd_input.send_keys(password)


# In[22]:


pwd_input.send_keys(Keys.RETURN)
#######################################


# In[23]:


####################################### Search through the bar


# In[24]:


##################################Go to twitter/explore
url = 'https://twitter.com/explore'
driver.get(url)


# In[27]:


#argument
# search_term = "Covid-19"
search_term = "BBC news"  #bug, needs to clear first, update later


#
xpath_search = '//input[@aria-label="Search query"]'
search_input = driver.find_element_by_xpath(xpath_search)
search_input.send_keys(search_term)
search_input.send_keys(Keys.RETURN)


# In[45]:


tab_name = "Latest" #argument
# tab_name = "People" #argument

tab = driver.find_element_by_link_text(tab_name)
tab.click()  #go to specific tab
xpath_tab_state = f'//a[contains(text(),\"{tab_name}\") and @aria-selected=\"true\"]'


# In[47]:


#collect tweets from current view

# testId = "UserCell"
testId = "tweet"
lookback_limit=25

page_cards = driver.find_elements_by_xpath(f'//div[@data-testid="{testId}"]')
card = page_cards[0]
# if len(page_cards) <= lookback_limit:
#     return page_cards
# else:
#     return page_cards[-lookback_limit:]


# In[48]:


#findusername
user = card.find_element_by_xpath('.//span').text  #give the first span after the current tag
print(user)


# In[49]:


#another test
card = page_cards[7]  #starts from 0, so the 8th
user = card.find_element_by_xpath('.//span').text  #give the first span after the current tag
print(user)


# In[50]:


#twitter handler; does not work
card = page_cards[0]
# card.find_element_by_xpath('.//span[contains(text(), "@")]').text

for card in page_cards:
    try:
        handle = card.find_element_by_xpath('.//span[contains(text(), "@")]').text
        print(handle)
        break
    except exceptions.NoSuchElementException:
        handle = ""


# In[51]:


postdate = card.find_element_by_xpath('.//time').get_attribute('datetime')
print(postdate)


# In[52]:


_comment = card.find_element_by_xpath('.//div[2]/div[2]/div[1]').text
print(_comment)


# In[53]:


_responding = card.find_element_by_xpath('.//div[2]/div[2]/div[2]').text
reply_count = card.find_element_by_xpath('.//div[@data-testid="reply"]').text
retweet_count = card.find_element_by_xpath('.//div[@data-testid="retweet"]').text
like_count = card.find_element_by_xpath('.//div[@data-testid="like"]').text


# In[54]:


print(_responding)
print(reply_count)
print(retweet_count)
print(like_count)


# In[55]:


driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#scroll down to the bottom


# In[ ]:




