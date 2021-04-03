import csv
import re

class get_hashtags(object):
    def __init__(self, pathToCSV):
        self.pathToCSV = pathToCSV
        with open(pathToCSV, 'r') as f:
            self.data = csv.reader(f)

    def GetHashtags(self):
        tweets = [x[3] for x in self.data]
        tweet_string = ' '.join(tweets)
        hashtags = re.findall(r'(^|\s)(#[a-z\d_]+)', tweet_string)
        return hashtags