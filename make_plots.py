import pandas as pd
import matplotlib as plt
import csv
import os
from wordcloud import WordCloud, STOPWORDS

class MakePlots(object):
    def __init__(self, pathToCSV):
        self.pathToCSV = pathToCSV
        self.makeplots()
        self.df = pd.read_csv(self.pathToCSV)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
    def makewordcloud(self):
        tweet_words = ''
        stopwords = set(STOPWORDS)
        for val in self.df.TweetText:
            val = str(val)
            tokens = val.split()
            for i in range(len(tokens)):
                tokens[i] = tokens[i].lower()
            tweet_words += " ".join(tokens) + " "
        
        wordcloud = WordCloud(width = 800, height = 800, background_color ='white', stopwords = stopwords, min_font_size = 10).generate(tweet_words)
        
        plt.figure(figsize = (8, 8), facecolor = None)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad = 0)
        
    def makeplots(self):
        # more code in future versions
        pass
        
    def showPlots(self):
        print(self.df.head(10))
        print(f"len: {len(self.df)}")
        plt.show()
        #more code in future versions


