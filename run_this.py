from twitter_scraper import TwitterScraper
from make_plots import MakePlots
import pyinputplus as pyip
import glob
#account used for scraping
#twitterscraper481@gmail.com
#password: Cnit481@

whichFunction = pyip.inputYesNo("Would you like to scrape the data: ")
if(whichFunction=="yes"):
    ts = TwitterScraper()

    #login is not required for scraping
    login = pyip.inputYesNo("Would you like to scrap after login: ")
    if(login == "yes"):
        twitterLogInLink = "https://twitter.com/login"
        # twitterAccountEmail = "twitterscraper481@gmail.com"
        twitterAccountEmail = pyip.inputEmail("Input your twitter account (email address): ")
        ts.login(twitterLogInLink, twitterAccountEmail)
    else:
        print("You choose not to log in.")
    # Specific User Scraping

    # userScraped="CDCgov"
    userScraped = pyip.inputStr("Type the specific user you would like to scrape: (for example: CDCgov)：")
    ts.searchByUser(userScraped)
    ts.close() #close the browser

else:
    print("You choose not to scrape.")

drawPlots = pyip.inputYesNo("Would you like to draw plots: ")
if(drawPlots=="yes"):
    #show all csv file paths
    print("Here are the list of CSV files:")
    pathToDataset = "./outputs"
    listAllcsv = []
    for filename in glob.glob(f"{pathToDataset}/*.csv"):
        print(filename)
    pathToCsvFile = pyip.inputFilepath("Type in the file path: ")
    # pathToCsvFile = "./outputs/CDCgov_posts_data.csv"
    pathToPlots = "./outputs/"
    mp = MakePlots(pathToCsvFile)
    mp.showDFhead()
    mp.makeLinePlot()
    mp.makeBarPlot()
    mp.makewordcloud()
    mp.makeHashtagWordCloud()
else:
    print("You choose not to draw plots.")


