import tushare
import tushare as ts
import datetime
import csv
import re
import os.path

tickersRawData = tushare.get_stock_basics()
tickers = tickersRawData.index.tolist()
dateToday = datetime.datetime.today().strftime('%Y-%m-%d')
if not os.path.isdir('Data'):
    os.makedirs('Data')
file = r'./Data/AllTickets'+dateToday+'.csv'
tickersRawData.to_csv(file)









# import tushare
# import tushare as ts
# import datetime
# import csv
# import re
#
#
# def getCode(fileName):
#     with open('D:\\Users\\Administrator\\'+fileName+'.csv', 'r', encoding='UTF-8') as f:
#         reader = csv.reader(f)
#         column = [row[0] for row in reader]
#         return column
#
# dateToday = datetime.datetime.today().strftime('%Y-%m-%d')
# column = getCode('10101000')    # 这里得到的是GetPoint80Tickers中保存的Point80
# print(column, len(column))
#
# def GetLowest(ticket, startT='2018-01-01',Distance = 30, rateDistance=1.08):
#     dateToday = datetime.datetime.today().strftime('%Y-%m-%d')
#     lowVaule = ''
#     history = ts.get_hist_data(ticket, start=startT)
#     op = history['open']
#     close = history['close']
#     low = history['low']
#     Week = ts.get_hist_data(ticket, ktype='W', start=startT)
#     WeekOpen = Week['open'][0]
#     WeekClose = Week['close'][0]
#     print(0000000, Week)
#     print("jjjjjj", Week['open'])
#     print("kkkkkkkk", Week['close'])
#     print("JJJJJJJjjjjjj", Week['open'][0])
#     print("KKKKKKKKkkkkkkkk", Week['close'][0])
#     # error = ts.get_hist_data("300423")['low']这一个是错的，这是为啥
#     # 已经有两个票是20181019最低点发起；600794，300158
#     # 获取历史最低价，然后得到相减的时间；
#     print(1, ticket, low)
#     print(len(low))
#     # a1=low.sort_values().index[0]
#     # a1 = ts.get_hist_data(column[i])['low'].sort_values().index[0]
#     a1 = low.sort_values().index[0]
#     print(2, a1)
#     d1 = datetime.datetime.strptime(a1, '%Y-%m-%d')
#     d2 = datetime.datetime.strptime(dateToday, '%Y-%m-%d')
#     # 此处直接用dateToday不可；类型不一致，# class 'str'>   # class 'datetime.datetime'>
#     # 简化，简化，简化；“300623”，值不对了，有问题；
#     valuesLow = low[a1]#这里处理最小值的是否有问题，可以同时获得array型数据的最小值及其对应的下标；
#     valuesNow = low[0]
#     print("2可以记录最低值", valuesLow, valuesNow)
#     print(3, a1, d1, d2)
#     print(type(d2))
#     print(type(d1))
#     DayDiff = (d2 - d1).days
#     print(DayDiff)
#     # //'300423在里是不合理的'调试，这个获取的股票数据都不对；重点关注
#     # 用len(low)>Distance, 排除 '603379', '600891', '300767'如这些新股；
#     if DayDiff < Distance or valuesNow <= rateDistance*valuesLow:
#         lowVaule = ticket
#
#     return lowVaule
#
# for i in column[:2]:
#     GetLowest(i)
#
# # 下一步如何在此处去掉st和新股；
# # tickersRawData = tushare.get_stock_basics()
# # tickers = tickersRawData.index.tolist()
# # dateToday = datetime.datetime.today().strftime('%Y-%m-%d')
# # file = 'D:\\Users\\Administrator\\Anaconda3'+dateToday+'.csv'
# # tickersRawData.to_csv(file)
#
#
# # def getPointTicker(ticker, growthRate=0.01):
# #     tickerName = ''
# #     history = ts.get_hist_data(ticker)
# #     op = history['open']
# #     close = history['close']
# #     # I think this one, can be, (close[0]>close[1] or open[0]>close[1] or hi>close[1]) and close[0]>op[0]
# #     # (close[0] - op[0]) / op[0] >= 1% and close[0] > close[1] the final
# #     if (close[0] - op[0]) / op[0] >= growthRate and (close[0] > close[1]):
# #             tickerName = ticker
# #     return tickerName
# #
# #
# # def saveCode(fileName, tickersList):
# #     with open('D:\\Users\\Administrator\\'+fileName+'.csv', 'w', encoding='UTF-8') as f:
# #         # 加上\n就不会报错，
# #         for i in tickersList:
# #             f.write(i + '\n')  # Terminate lines with \n 使用\ n终止行
# #
# #
# # def getCode(fileName):
# #     with open('D:\\Users\\Administrator\\'+fileName+'.csv', 'r', encoding='UTF-8') as f:
# #         reader = csv.reader(f)
# #         column = [row[0] for row in reader]
# #         return column
# #
# #
# # def filterCode(ticker):
# #     tickerName = ''
# #     history = ts.get_hist_data(ticker)
# #     op = history['open']
# #     tickerReName = ts.get_realtime_quotes(ticker)['name'][0]
# #     print(tickerReName)
# #     print(len(op))
# #     if re.match(r'[*stST]', tickerReName) and len(op) > 20:
# #         tickerName = '88888888'
# #     return tickerName
# #
# # print(11111111111)
# # print(filterCode('002070'))
# # print(222222222222)
# # print(filterCode('000050'))
# # tickerReName = ts.get_realtime_quotes('002070')['name'][0]
# # tickerReName1 = ts.get_realtime_quotes('000050')['name'][0]
# # tickerReName2 = 'ST大可'
# # print(type(tickerReName))
# # print(re.match(r'[*stST]', tickerReName))
# # print(re.match(r'[*stST]', tickerReName1))
# # print(re.match(r'[*stST]', tickerReName2))
# # print(type(re.match(r'[*stST]', tickerReName)))
# #
# # if re.match(r'[*stST]', tickerReName1) == None:
# #     print("quick quick")
# #
# #
# # def filterCode(ticker, tickerDay):
# #     tickerReName = ts.get_realtime_quotes(ticker)['name'][0]
# #     print(tickerReName)
# #     # re.match()若匹配成功返回一个Match对象，否则返回None
# #     if re.match(r'[*stST]', tickerReName) == None and tickerDay > 20:
# #         return True
# #
# #
# # print(filterCode('000050', 30))
# # print(filterCode('002070', 30))
# # if filterCode('000050', 30):
#     print("12342355")