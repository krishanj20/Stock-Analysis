import pandas as pd
import pandas_datareader as pdr
import numpy as np
import matplotlib.pyplot as plt
import csv

def GetPrices(InFile, OutFile):
    #Open inFile
    with open(InFile) as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            ticker = row
            del ticker[0]
            
    # Pulling Data
    data = []
    for i in range(len(ticker)):
        data.append(
            pdr.get_data_tiingo(ticker[i], api_key='bf2663618907db14116db19a8108c44b96a1a37d',
                                    start='2015-01-01', end='2020-01-01'))
    
    #Cleaning
    Prices = []
    for df in data:
        df.reset_index(inplace=True)
        df.index = pd.to_datetime(df['date'])
        Prices.append(df['adjClose'])
    stockPrices = pd.concat(Prices, axis=1)
    stockPrices.columns = ticker
    stockPrices.to_csv(OutFile)
    print('Prices obtained for ' + InFile)

GetPrices('tickers.csv', 'Prices.csv')