import pandas
import matplotlib
import mpl_finance    # inside matplotlib.finance
import matplotlib.pyplot as plt
import csv
import tushare
import datetime
import os
import tushare as ts
from A1TwoRelax import Continuous90


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
        j = 0
        k = 0
        number = 0

        while j == 0:
            if (close[j]-op[j]) / op[j] >= 0.02:
                print("number am counting")
                number += 1
            print("0j am counting")
            j += 1

        if number >= 1:
            L.append(column[i])
            LNumber.append(i)

        print("i am counting")
        i += 1
        print(L, len(L))
        print(LNumber, i)
 
    except:
        i += 1
        continue

# Notice: the value of two function is not same, get_hist_data, get_realtime_quotes
OnePlus80 = []
OnePlus90 = []

for this in L:
    thisYesterday = ts.get_hist_data(this)
    closeYesterday = thisYesterday['close'][0]
    openYesterday = thisYesterday['open'][0]
    thisToday = ts.get_realtime_quotes(this)
    openToday = thisToday['open'][0]
    priceToday = thisToday['price'][0]
    lowToday = thisToday['low'][0]
    openTodayValue = float(openToday)
    priceTodayValue = float(priceToday)
    lowTodayValue = float(lowToday)

    if openTodayValue / closeYesterday >= 0.98 and lowTodayValue >= openYesterday:
        OnePlus80.append(this)
        if lowTodayValue >= closeYesterday:
            OnePlus90.append(this)

print("OnePlus80", OnePlus80)
print("OnePlus90", OnePlus90)
print("OnePlus80, not 90: ", list(set(OnePlus80).difference(set(OnePlus90))))
print("Continuous90: ", Continuous90)
print("OnePlus90: ", OnePlus90)
print("One+Two_90: ", list(set(OnePlus90).intersection(set(Continuous90))))
