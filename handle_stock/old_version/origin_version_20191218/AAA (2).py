import pandas
import matplotlib
import mpl_finance    # inside matplotlib.finance
import matplotlib.pyplot as plt
import csv
import tushare
import datetime
import os
import tushare as ts


def getCode(fileName):
    with open('D:\\Users\\Administrator\\'+fileName+'.csv', 'r', encoding='UTF-8') as f:
        reader = csv.reader(f)
        column = [row[0] for row in reader]
        return column


dateToday = datetime.datetime.today().strftime('%Y%m%d')
column = getCode('Anaconda3' + dateToday)
i = 1
L = []
LNumber = []

while i < len(column):
    try:
        history = ts.get_hist_data(column[i])
        op = history['open']
        close = history['close']
        low = history['low']
        k = 0
        number = 0

        if (close[0]-op[0]) / op[0] >= 0.02 or (low[0] > close[1] and low[0] > op[1]):
            number += 1

        if number >= 1:
            L.append(column[i])
            LNumber.append(i)

        i += 1
        print(L)
        print(LNumber, len(L), i)
 
    except:
        i += 1
        continue

# Notice: the value of two function is not same, get_hist_data, get_realtime_quotes
Point80 = []
Point90 = []
Point95 = []

for this in L:
    try:
        thisYesterday = ts.get_hist_data(this)
        closeYesterday = thisYesterday['close'][0]
        openYesterday = thisYesterday['open'][0]
        highYesterday = thisYesterday['high'][0]
        closeBeforeY = thisYesterday['close'][1]
        openBeforeY = thisYesterday['open'][1]
        thisToday = ts.get_realtime_quotes(this)
        openToday = thisToday['open'][0]
        priceToday = thisToday['price'][0]
        lowToday = thisToday['low'][0]
        openTodayValue = float(openToday)
        priceTodayValue = float(priceToday)
        lowTodayValue = float(lowToday)

        if openTodayValue / closeYesterday >= 0.98 and lowTodayValue >= openYesterday:
            Point80.append(this)
            if lowTodayValue >= closeYesterday and (closeBeforeY - openBeforeY) / openBeforeY >= 0.01:
                Point90.append(this)
                if lowTodayValue > highYesterday:
                    Point95.append(this)

    except:
        continue

OnlyScore80 = list(set(Point80).difference(set(Point90)))
OnlyScore90 = list(set(Point90).difference(set(Point95)))

print("OnlyScore80: ", OnlyScore80)
print("OnlyScore90: ", OnlyScore90)
print("OnlyScore95: ", Point95)


