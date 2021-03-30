from twitter_scraper import TwitterScraper
from make_plots import MakePlots


ts = TwitterScraper()

# # login is not required
# twitterLogInLink = "https://twitter.com/login"
# twitterAccountEmail = "xiaxin.shen@outlook.com"
# ts.login(twitterLogInLink, twitterAccountEmail)
#
# Specific User Scraping
userScraped="CDCgov"
ts.searchByUser(userScraped)

#draw plots
# pathToCsvFile = ts.getFilename()
pathToCsvFile = "./outputs/CDCgov_posts_data.csv"
mp = MakePlots(pathToCsvFile)
mp.showPlots()

