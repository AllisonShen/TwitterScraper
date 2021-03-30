import pandas as pd
import matplotlib as plt
import csv
import os

class MakePlots(object):
    def __init__(self, pathToCSV):
        self.pathToCSV = pathToCSV
        self.makeplots()
        self.df = pd.read_csv(self.pathToCSV)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
    def makeplots(self):
        pass

    def showPlots(self):
        print(self.df.head(10))
        print(f"len: {len(self.df)}")


