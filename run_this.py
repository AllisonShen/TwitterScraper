from twitter_scraper import TwitterScraper

ts = TwitterScraper()

# when login needed
ts.login("https://twitter.com/login", "xiaxin.shen@outlook.com")
# Specific User Scraping
userScraped="CDCgov"
ts.searchByUser(userScraped)

'''
How to do scraping without login (needs to be figured out)
'''