import pandas
import matplotlib
import mpl_finance    #inside matplotlib.finance
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
        # print(column)
column = getCode('Anaconda320190313')
column1 = column[1:]

i = 1
L = []
LNumber = []

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

        while j < 2:

            if close[j] > op[j] and close[j] > close[j + 1] and op[j] > op[j + 1] and (close[j] - op[j]) / op[j] > 0.01:
                print("number am counting")
                number += 1

            print("j am counting")
            j += 1

        if number >= 2:
            L.append(column[i])
            LNumber.append(i)

        print("i am counting")
        i += 1
        print(L, i)
        print(LNumber)
        print(len(L))


    except:
        i += 1
        continue
# Notice: the value of two function is not same, get_hist_data, get_realtime_quotes
Continuous80 = []
Continuous90 = []
Continuous95 = []
for this in L:
    thisYesterday = ts.get_hist_data(this)
    closeYesterday = thisYesterday['close'][1]
    openYesterday = thisYesterday['open'][1]
    thisToday = ts.get_realtime_quotes(this)
    openToday = thisToday['open'][0]
    priceToday = thisToday['price'][0]
    lowToday = thisToday['low'][0]
    openTodayValue = float(openToday)
    priceTodayValue = float(priceToday)
    lowTodayValue = float(lowToday)

    if openTodayValue >= closeYesterday or priceTodayValue >= closeYesterday:
        Continuous80.append(this)
        if lowTodayValue >= openYesterday and openTodayValue >= closeYesterday:
            Continuous90.append(this)
            if lowTodayValue >= closeYesterday:
                Continuous95.append(this)

print("Continuous80, not 90: ", list(set(Continuous80).difference(set(Continuous90))))
print("Continuous90, not 95: ", list(set(Continuous90).difference(set(Continuous95))))
print("Continuous95: ", Continuous95)
