import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import pandas_datareader
import pandas_datareader.data as web
import datetime

##Start and end dates
start = datetime.datetime(2016,3,31)
end = datetime.datetime(2018,3,31)

##Stocks
boeing = web.DataReader('BA','morningstar', start, end)
lockheed = web.DataReader("LMT", 'morningstar', start, end)
raytheon = web.DataReader('RTN', 'morningstar', start, end)
boeing.index = pd.to_datetime(boeing.index.levels[1], unit='d')
lockheed.index = pd.to_datetime(lockheed.index.levels[1], unit='d')
raytheon.index = pd.to_datetime(raytheon.index.levels[1], unit='d')

##Opening prices
lockheed['Open'].plot(label = 'Lockheed Martin', figsize=(16,8), title = 'Opening Prices')
raytheon['Open'].plot(label = 'Raytheon')
boeing['Open'].plot(label = "Boeing")
plt.title("Opening Prices")
plt.xlabel('Date')
plt.ylabel('Return (%)')
plt.legend()
plt.show()


##RTN Moving Averages
raytheon['MA30'] = raytheon['Open'].rolling(30).mean()
raytheon['MA50'] = raytheon['Open'].rolling(50).mean()
raytheon['MA200'] = raytheon['Open'].rolling(200).mean()
raytheon[['Open', 'MA30', 'MA50', 'MA200']].plot(figsize = (16,8))
plt.title("Raytheon Moving Average")
plt.xlabel('Date')
plt.ylabel('RTN Stock Price')
plt.legend()
plt.show()

#Daily Returns
lockheed['returns'] = lockheed['Close'].pct_change(1)
boeing['returns'] = boeing['Close'].pct_change(1)
raytheon['returns'] = raytheon['Close'].pct_change(1)

##Histogram
boeing['returns'].hist(bins = 100, label = "Boeing", figsize = (10,8), alpha = 0.7)
raytheon['returns'].hist(bins = 100, label = "Raytheon", figsize = (10,8), alpha = 0.7)
lockheed['returns'].hist(bins = 100, label = "Lockheed Martin", figsize = (10,8), alpha = 0.7)
plt.legend()
plt.title("Daily Returns")
plt.xlabel("Daily Return")
plt.ylabel("Frequency (%)")
plt.show()

#Kernel density estimation
lockheed['returns'].plot(kind = 'kde',label = "Lockheed Martin", figsize = (10,8))
boeing['returns'].plot(kind = 'kde',label = "Boeing", figsize = (10,8))
raytheon['returns'].plot(kind = 'kde',label = "Raytheon", figsize = (10,8))
plt.title("Daily Returns")
plt.xlabel("Daily Return")
plt.ylabel("Frequency (%)")
plt.legend()
plt.show()

#Box plot
box_df = pd.concat([lockheed['returns'], boeing['returns'], raytheon['returns']], axis = 1)
box_df.columns = ['Lockheed Martin Returns', 'Boeing Returns', 'Raytheon Returns']
box_df.plot(kind='box', figsize = (8,11))
plt.title("Daily Returns")
plt.xlabel("Daily Returns")
plt.show()

#Cumulative returns
lockheed['Cumulative Returns'] = (1+lockheed["returns"]).cumprod()
boeing['Cumulative Returns'] = (1+boeing["returns"]).cumprod()
raytheon['Cumulative Returns'] = (1+raytheon["returns"]).cumprod()

lockheed['Cumulative Returns'].plot(label = "Lockheed Martin")
raytheon['Cumulative Returns'].plot(label = "Raytheon")
boeing['Cumulative Returns'].plot(label = "Boeing")
plt.xlabel('Date')
plt.ylabel("Cumulative Return")
plt.title("Cumulative Returns")
plt.legend()
plt.show()

