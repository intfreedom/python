# import pandas
# import matplotlib
# import mpl_finance    #inside matplotlib.finance
# import matplotlib.pyplot as plt
# import csv
# import tushare
# import datetime
# import os
# import tushare as ts

L = [1, 11, 34, 2, 8, 9]

print(11 > 0.9*L[1])
for i in L:
    if i >= 8:
        print(80, i)
        if i<15:
            print(90,   i)
            if i > 10:
                print(95, i)


# print(list(set(Continuous90).difference(set(Continuous95))))
# thisYesterday = ts.get_hist_data('600179')
# closeYesterday = thisYesterday['close'][0]
# print(closeYesterday)
# thisToday = ts.get_realtime_quotes('600179')
# openToday = thisToday['open'][0]
# print(thisToday['price'][0])
# print(openToday)
# if openToday >= closeYesterday:
#     print("f mm")
# def getCode(fileName):
#     with open('D:\\Users\\Administrator\\'+fileName+'.csv', 'r', encoding='UTF-8') as f:
#         reader = csv.reader(f)
#         column = [row[0] for row in reader]
#         return column
# # column = getCode('Anaconda320190309')
# def getLowestPrice(ticker, start='2018-01-01'):
#     history = ts.get_hist_data(ticker, start)
#     low = history['low']
#     lowestPrice = low.nsmallest(1).values[0]
#     return lowestPrice
#
# def getLowestPriceFive(ticker):
#     history = ts.get_hist_data(ticker)
#     lowFive = history['low'][0:5]
#     lowestPriceFive = lowFive.nsmallest(1).values[0]
#     return lowestPriceFive
#
# pLowest = getLowestPrice('601608')
# pFive = getLowestPriceFive('601608')
# print(pFive, pLowest)
# history = ts.get_hist_data('600072')
# print(type(history))
# print(history)
# print(history[0:3])
# print(history['low'][0:3])
# print(history[0:3]['low'])
# i = 1
# L = []
# LNumber = []
#
# while i < len(column):
#     # history = ts.get_hist_data('600072')
#     history = ts.get_hist_data(column[i])
#
#     try:
#         op = history['open']
#         close = history['close']
#         j = 0
#         k = 0
#         number = 0
#
#         while j < 4:
#
#             if close[j] > op[j] and close[j] > close[j + 1] and op[j] > op[j + 1] and (close[j] - op[j]) / op[j] > 0.01:
#                 print("number am counting")
#                 number += 1
#
#             print("j am counting")
#             j += 1
#
#         if number >= 3:
#             L.append(column[i])
#             LNumber.append(i)
#
#         print("i am counting")
#         i += 1
#         print(L, i)
#         print(LNumber)
#
#
#     except:
#         i += 1
#         continue

# import datetime
# dateToday = (datetime.datetime.today()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d')
# print(dateToday)
#
# def getLowestPrice():
#     history = [1,2,3]
#
#     lowestPrice = min(history)
#     return lowestPrice
# print(getLowestPrice())
# print(2/3)
# list = [12,33,55]
# print("I am ok: ", list)
# # column = [1, 5, 6, 217, 219, 2110, 2111, 2112, 2115, 16, 18]
# # open = [11, 15, 16, 17, 19, 110, 111, 112, 115, 116, 118]
# # i = 1
# # while i < len(column):
# #     j = 0
# #     k = 0
# #     number = 0
# #     while j < 5:
# #         if column[j] < open[j]:
# #             print("number am counting")
# #             number += 1
# #
# #             # while close[j] > close[j + 1]:
# #             #     number += 1
# #         if number >= 3:
# #             print("yes")
# #
# #         print("j am counting")
# #         j += 1
# #     print("i am counting")
# #     i += 1
# #     print(number)
# #
# # if 3<5 and 3>2 and 3>1:
# #     print("OKokokokok")
# # if (6.30-5.73)/5.73 > 0.01:
# #     print("dayedi")
# # print((6.30-5.73)/5.73)
# #
