import pandas as pd
import matplotlib as plt
import csv
'''
df = pd.read_csv(pathToCsvFile)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df.head(10)
'''
class MakePlots(object):
    def __init__(self, pathToCSV):
        self.pathToCSV = pathToCSV
        self.makeplots()
    def makeplots(self):
        pass
    def showPlots(self):
        pass

