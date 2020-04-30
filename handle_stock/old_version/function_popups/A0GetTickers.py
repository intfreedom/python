import tushare
import pandas
import datetime
import os
import csv
import codecs

def stockPriceIntraday(ticker, folder):
    # Step 1. Get intrady data online
    intrady = tushare.get_hist_data(ticker, ktype='5')

    # Step 2. If the history exists, append
    file = folder+'\\'+ticker+'.csv'
    if os.path.exists(file):
        history = pandas.read_csv(file, index_col=0)
        intrady.append(history)

    # Step 3. Inverse based on index
    intrady.sort_index(inplace=True)
    intrady.index.name ='timestamp'

    # Step 4. Save
    intrady.to_csv(file)
    print('Intraday for ['+ticker+'] got.')

# Step 1.Get tickers online
tickersRawData = tushare.get_stock_basics()    #type is <class 'pandas.core.frame.DataFrame'>
tickers = tickersRawData.index.tolist()    #type is <class 'method'>实际变为列表了，为何type
#type is <class 'pandas.core.frame.DataFrame'>这种数据类型可以利用to_csv函数；list不可以；
#Step 2. Save the ticker list to a local file
dateToday = datetime.datetime.today().strftime('%Y-%m-%d')
file = 'D:\\Users\\Administrator\\Anaconda3'+dateToday+'.csv'
tickersRawData.to_csv(file)

for i, ticker in enumerate(tickers):
    try:
        print('Intrady',i,'/',len(tickers))
        stockPriceIntraday(ticker, folder='D:\\Users\\Administrator')
    except:
        pass

print('Tickers saved.')
