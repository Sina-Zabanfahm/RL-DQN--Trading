# -*- coding: utf-8 -*-
"""Reader.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14oMcqIJIF2yMd60wYGXI8n2kQszMXryK
"""

import pandas as pd
import numpy as no
import matplotlib.pyplot as plt

import yfinance as yf
import json

class DataReader:

    def __init__(self, ticker = 'SPY', start_date = '2012-03-01', end_date = '2023-01-01'):

      self.ticker = ticker
      self.start_date = start_date
      self.end_date = end_date

      self.data = pd.DataFrame()

    def read_data(self):

      self.data = yf.download(self.ticker, self.start_date, self.end_date)
      self.data = self.data[['Open']]
      self.data.dropna(axis = 1, inplace = True)
      self.data.set_index (pd.to_datetime(self.data.index), inplace = True)

    def get_data(self):

      return self.data

    def geta_dates(self):

      return [self.start_date, self.end_date]