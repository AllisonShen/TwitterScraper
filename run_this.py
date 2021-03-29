#run this file at terminal for typing the password successfully

from twitter_scraper import TwitterScraper

# when login needed
ts = TwitterScraper()
ts.login("https://twitter.com/login", "xiaxin.shen@outlook.com")


#when login not needed
'''
How to do scraping without login (needs to be figured out)
'''

##############################################################
userScraped="CDCgov"
ts.searchByUser(userScraped)