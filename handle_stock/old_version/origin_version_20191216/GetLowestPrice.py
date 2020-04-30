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
dateToday = datetime.datetime.today().strftime('%Y-%m-%d')
def getLowestPrice(ticker, start='2018-01-01'):
    history = ts.get_hist_data(ticker, start)
    low = history['low']
    lowestPrice = low.nsmallest(1).values[0]
    return lowestPrice

def getLowestPriceFive(ticker):
    history = ts.get_hist_data(ticker)
    lowFive = history['low'][0:5]
    lowestPriceFive = lowFive.nsmallest(1).values[0]
    return lowestPriceFive

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

            if close[j] > op[j] and close[j] > close[j + 1] and op[j] > op[j + 1] and (close[j] - op[j]) / op[j] > 0.02:
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

def lowestFiveProportion(pLowest, pFive, proportion):
    if pLowest/pFive >= proportion:
        return True

# dateFive = (datetime.datetime.today() + datetime.timedelta(days=-5)).strftime('%Y-%m-%d')
youCan80 = []
youCan90 = []
youCan95 = []
LyouCan85 = []
LyouCan90 = []
LyouCan95 = []

for ticker in L:
    try:
        pLowest = getLowestPrice(ticker)
        pFive = getLowestPriceFive(ticker)
        if lowestFiveProportion(pLowest, pFive, 0.8):
            youCan80.append(ticker)
        if lowestFiveProportion(pLowest, pFive, 0.9):
            youCan90.append(ticker)
        if lowestFiveProportion(pLowest, pFive, 0.95):
            youCan95.append(ticker)
    except:
        pass

for ticker in column1:
    try:
        print(ticker, "go on, go on")
        pLowest = getLowestPrice(ticker)
        pFive = getLowestPriceFive(ticker)
        if lowestFiveProportion(pLowest, pFive, 0.85):
            LyouCan85.append(ticker)
        if lowestFiveProportion(pLowest, pFive, 0.9):
            LyouCan90.append(ticker)
        if lowestFiveProportion(pLowest, pFive, 0.95):
            LyouCan95.append(ticker)
    except:
        pass
print(len(L), L)
print("you can 80: ", youCan80)
print("you can 90: ", youCan90)
print("you can 95: ", youCan95)
print("Low you can 85: ", LyouCan85)
print("Low you can 90: ", LyouCan90)
print("Low you can 95: ", LyouCan95)
