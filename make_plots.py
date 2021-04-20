import pandas as pd
import matplotlib.pyplot as plt
import csv
import os
from wordcloud import WordCloud, STOPWORDS
#pip install seaborn
import seaborn as sns
import datetime
import re

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
        plotname = f"./outputs/wordcloud.png"

        plt.savefig(plotname)
        plt.show()
        plt.close()
    
    def makeHashtagWordCloud(self):
        tweet_words = ''
        for val in self.df.TweetText:
            val = str(val)
            tokens = val.split()
            for i in range(len(tokens)):
                tokens[i] = tokens[i].lower()
            tweet_words += " ".join(tokens) + " "
        hashtags = re.findall(r'(?:^|\s)(#[a-z\d_]+)', tweet_words)
        stopwords = set(STOPWORDS)
        hashtag_string = ''
        hashtag_string += " ".join(hashtags) + " "
        wordcloud = WordCloud(width = 800, height = 800, background_color ='white', stopwords = stopwords, min_font_size = 10).generate(hashtag_string)
        
        plt.figure(figsize = (8, 8), facecolor = None)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad = 0)
        plotname = f"./outputs/wordcloud_hashtags.png"

        plt.savefig(plotname)
        plt.show()
        plt.close()
        
    def makeLinePlot(self):
        # self.df['Date'] = self.df['PostDate'].map(lambda x: x.date())
        # df_groupedby_date = self.df.groupby('Date').count()
        # df_groupedby_date.reset_index(inplace=True)
        # plt.plot_date(x=df_groupedby_date['Date'], y=df_groupedby_date['Value'])
        self.df['Date'] = pd.to_datetime(self.df['PostDate'], errors = 'coerce')
        # self.df['ReplyCount'] = pd.to_numeric(self.df['ReplyCount'])
        self.df['ReplyCount'] = self.df['ReplyCount'].apply(value_to_float)
        print(type(self.df['Date']))
        # print(self.df['Date'])
        print(self.df['ReplyCount'])
        graph = sns.lineplot(data=self.df,x='Date',y='ReplyCount')
        date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M")
        # plotname = f"./outputs/plot_line_{date_string}.png"
        plotname = f"./outputs/plot_line.png"

        plt.savefig(plotname)
        plt.show()
        plt.close()
        # sns.lmplot(x='Date', y='ReplyCount')


        pass
    def makeplots(self):
        # more code in future versions
        pass
        
    def showPlots(self):
        print(self.df.head(10))
        print(f"len: {len(self.df)}")
        plt.show()
        #more code in future versions

def value_to_float(x):
    if type(x) == float or type(x) == int:
        return x
    if 'K' or 'k' in x:
        if len(x) > 1:
            return float(x.replace('K', '')) * 1000
        return 1000.0
    if 'M' or 'm' in x:
        if len(x) > 1:
            return float(x.replace('M', '')) * 1000000
        return 1000000.0
    if 'B' or 'b' in x:
        return float(x.replace('B', '')) * 1000000000
    return 0.0


