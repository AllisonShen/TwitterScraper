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
    def makeplots(self, strType):
        date_string = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M")
        plotname = f"./outputs/plot_{strType}_{date_string}.png"
        # plotname = f"./outputs/plot_line.png"
        plt.savefig(plotname)
        plt.show()
        plt.close()
    def makeLinePlot(self):
        self.df['Date'] = pd.to_datetime(self.df['PostDate'], errors = 'coerce')
        #######ReplyCount
        self.df['ReplyCount'] = self.df['ReplyCount'].apply(value_to_float)

        fig, ax = plt.subplots(figsize=(12, 6))
        fig = sns.lineplot(x='Date',y='ReplyCount', data=self.df,
                          estimator=sum, ci=None, ax=ax)

        self.makeplots("line_replycount")
        #########LikeCount
        self.df['LikeCount'] = self.df['LikeCount'].apply(value_to_float)
        fig, ax = plt.subplots(figsize=(12, 6))
        fig = sns.lineplot(x='Date',y='LikeCount', data=self.df,
                          estimator=sum, ci=None, ax=ax)

        self.makeplots("line_likecount")
        ########RetweetCount
        self.df['RetweetCount'] = self.df['RetweetCount'].apply(value_to_float)
        fig, ax = plt.subplots(figsize=(12, 6))
        fig = sns.lineplot(x='Date', y='RetweetCount', data=self.df,
                           estimator=sum, ci=None, ax=ax)

        self.makeplots("line_RetweetCount")
    def makeBarPlot(self):
        self.df['Date'] = pd.to_datetime(self.df['PostDate'], errors = 'coerce')
        ###########ReplyCount
        self.df['ReplyCount'] = self.df['ReplyCount'].apply(value_to_float)
        fig, ax = plt.subplots(figsize=(12, 6))
        fig = sns.barplot(x="Date", y="ReplyCount", data=self.df,
                          estimator=sum, ci=None, ax=ax)

        self.makeplots("bar_replycount")

        #########LikeCount
        self.df['LikeCount'] = self.df['LikeCount'].apply(value_to_float)
        fig, ax = plt.subplots(figsize=(12, 6))
        fig = sns.barplot(x="Date", y="LikeCount", data=self.df,
                          estimator=sum, ci=None, ax=ax)
        self.makeplots("bar_likecount")

        #########RetweetCount
        self.df['RetweetCount'] = self.df['RetweetCount'].apply(value_to_float)
        fig, ax = plt.subplots(figsize=(12, 6))
        fig = sns.barplot(x="Date", y="RetweetCount", data=self.df,
                          estimator=sum, ci=None, ax=ax)
        self.makeplots("bar_RetweetCount")
    def showDFhead(self):
        print(self.df.head(10))
        print(f"len: {len(self.df)}")
        plt.show()
        #more code in future versions

def value_to_float(x):
    if type(x) == float or type(x) == int:
        return x
    if 'K' or 'k' in x:
        return float(x.replace('K', '')) * 1000
    if 'M' or 'm' in x:
        return float(x.replace('M', '')) * 1000000
    if 'B' or 'b' in x:
        return float(x.replace('B', '')) * 1000000000
    return 0.0


