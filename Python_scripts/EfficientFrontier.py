#Import libraries to be used in code
import sys
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def EfficientFrontier(InFile):
    stocks = pd.read_csv(InFile, index_col = 0)
    ticker = stocks.columns.tolist()
    # Log returns and covariance needed for the Sharpe Ratio 
    log_returns = np.log(stocks/stocks.shift(1))
    log_returns.dropna(inplace=True)


    log_returns.cov() * 252
    # Generating a random set of normalised weights
    weights = np.array(np.random.random(5))
    weights = weights/np.sum(weights)
    weights

    # Variable that determines number of random portfolios to generate
    num_portfolios = 10000

    # Defining the arrays to "store" all our random portfolio and their statistics in its ith position
    weights_array = np.zeros((num_portfolios, len(stocks.columns)))
    returns_array = np.zeros(num_portfolios)
    vol_array = np.zeros(num_portfolios)
    sharpe_array = np.zeros(num_portfolios)

    for i in range(num_portfolios):
        weights = np.array(np.random.random(5))
        weights = weights/np.sum(weights)
        
        #Storing the portfolio weights/returns/vol/sharpe ratio in the ith position
        weights = weights_array[i,:] = weights
        
        returns_array[i] = np.sum(log_returns.mean()*252*weights)
        
        vol_array[i] = np.sqrt(np.dot(weights.T,np.dot(log_returns.cov()*252,weights)))
        
        sharpe_array[i] = returns_array[i]/vol_array[i]

    sns.set()

    max_SR_return = returns_array[sharpe_array.argmax()]
    max_SR_vol = vol_array[sharpe_array.argmax()]

    plt.scatter(vol_array,returns_array,c=sharpe_array,cmap='coolwarm')
    plt.colorbar(label='Sharpe Ratio')
    plt.scatter(max_SR_vol, max_SR_return,c='yellow',edgecolors='black',s=70)
    plt.xlabel('Volatility')
    plt.ylabel('Returns')
    plt.title('Efficient Frontier')
    plt.savefig('Outputs/Efficient_Frontier.png')

    plt.pie(weights_array[sharpe_array.argmax()], labels = ticker, autopct='%1.1f%%')
    plt.savefig('Outputs/Portfolio_share.png')

EfficientFrontier('Prices.csv')