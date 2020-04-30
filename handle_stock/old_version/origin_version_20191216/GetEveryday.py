import pandas
import matplotlib
import mpl_finance    #inside matplotlib.finance
import matplotlib.pyplot as plt
import csv
import tushare
import datetime
import os
import tushare as ts

#
# def stockPriceIntraday(ticker, folder):
#     # Step 1. Get intrady data online
#     intrady = tushare.get_hist_data(ticker, ktype='5')
#
#     # Step 2. If the history exists, append
#     file = folder+'\\'+ticker+'.csv'
#     if os.path.exists(file):
#         history = pandas.read_csv(file, index_col=0)
#         intrady.append(history)
#
#
#     # Step 3. Inverse based on index
#     intrady.sort_index(inplace=True)
#     intrady.index.name ='timestamp'
#
#     # Step 4. Save
#     intrady.to_csv(file)
#     print('Intraday for ['+ticker+'] got.')
#
# # Step 1.Get tickers online
# tickersRawData = tushare.get_stock_basics()
# tickers = tickersRawData.index.tolist()
#
# #Step 2. Save the ticker list to a local file
# dateToday = datetime.datetime.today().strftime('%Y%m%d')
#
# file = 'D:\\Users\\Administrator\\Anaconda3'+dateToday+'.csv'
# tickersRawData.to_csv(file)
#
#
# for i, ticker in enumerate(tickers):
#     try:
#         print('Intrady',i,'/',len(tickers))
#         stockPriceIntraday(ticker, folder='D:\\Users\\Administrator')
#     except:
#         pass
#     if i>300000:
#         break
# print('Tickers saved.')
def getCode(fileName):
    with open('D:\\Users\\Administrator\\'+fileName+'.csv', 'r', encoding='UTF-8') as f:
        reader = csv.reader(f)
        column = [row[0] for row in reader]
        return column
        # print(column)
column = getCode('Anaconda320190309')

i = 1
L = []
LNumber = []
# history = ts.get_hist_data('601608', start='2013-01-01')
# print(history)
while i < len(column):
    history = ts.get_hist_data(column[i])
    # if history is None:
    #     i += 1
    #     continue
    try:
        op = history['open']
        close = history['close']
        j = 0
        k = 0
        number = 0

        while j < 3:

            if close[j] > op[j] and close[j] > close[j + 1] and op[j] > op[j + 1] and (close[j] - op[j]) / op[j] > 0.01:
                print("number am counting")
                number += 1

            print("j am counting")
            j += 1

        if number >= 3:
            L.append(column[i])
            LNumber.append(i)

        print("i am counting")
        i += 1
        print(L, i)
        print(LNumber)


    except:
        i += 1
        continue
