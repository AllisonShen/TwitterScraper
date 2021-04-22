from twitter_scraper import TwitterScraper
from make_plots import MakePlots
import pyinputplus as pyip

#account used for scraping
#twitterscraper481@gmail.com password: Cnit481@

whichFunction = pyip.inputYesNo("Would you like to scrape the data: ")
if(whichFunction=="yes"):
    ts = TwitterScraper()
    login = pyip.inputLogin("Would you like to scrap after login: ")
    if(login == "yes"):
        twitterLogInLink = "https://twitter.com/login"
        # twitterAccountEmail = "twitterscraper481@gmail.com"
        twitterAccountEmail = pyip.inputEmail("Input your twitter account (email address): ")
        ts.login(twitterLogInLink, twitterAccountEmail)
    else:
        print("You choose not to log in.")
else:
    print("You choose not to scrape.")

# ts = TwitterScraper()
#
# # login is not required
# twitterLogInLink = "https://twitter.com/login"
# twitterAccountEmail = "xiaxin.shen@outlook.com"
# ts.login(twitterLogInLink, twitterAccountEmail)
#
# # Specific User Scraping
# userScraped="CDCgov"
# ts.searchByUser(userScraped)
# ts.close() #close the browser



#draw plots
# pathToCsvFile = ts.getFilename()
pathToCsvFile = "./outputs/CDCgov_posts_data.csv"
pathToPlots = "./outputs/"
mp = MakePlots(pathToCsvFile)
mp.makeLinePlot()
mp.makeBarPlot()

# mp.makewordcloud()
# mp.makeHashtagWordCloud()
# mp.showDFhead()

