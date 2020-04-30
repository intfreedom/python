import csv
import datetime
import tushare as ts
from GetLowestPrice import GetLowest
from GetContinusRise import continuous
# 从20180101至今，所有最小值至今差距20天内的，所用低票价在3元以内的；
Lowest90 = []
OneYuan = []
Point80 = []
Point90 = []
Point95 = []
MVP = []

N = 0 #相当于查看进度，一共3600只；
def getCode(fileName):
    with open(r'./Data/'++fileName+'.csv', 'r', encoding='UTF-8') as f:
        reader = csv.reader(f)
        column = [row[0] for row in reader]
        return column

dateToday = datetime.datetime.today().strftime('%Y-%m-%d')
# column = getCode('AllTickets')    # 这里得到的是all tickets
column = getCode('10101000')    # 这里得到的是GetPoint80Tickers中保存的Point80
# column = getCode('10101000-Point90')  #10101000-Point90
print(column)

for i in column:
    # try:
    #     ticketL = GetLowest(i)
    #     if ticketL[1] != '':
    #         Lowest90.append(ticketL[1])
    #     if ticketL[0] != '':
    #         OneYuan.append(ticketL[0])
    #     print(Lowest90, OneYuan, N)
    # except:
    #     continue

    try:
        ticketC = continuous(i)
        if ticketC[0] != '':
            Point80.append(ticketC[0])
        print(Point80, N)
        if ticketC[1] != '':
            Point90.append(ticketC[1])
            if GetLowest(i)[1] != '':
                MVP.append(i)
        # if ticketC[2] != '':
        #     Point95.append(ticketC[2])
    except:
        continue

    N += 1
OnlyScore80 = list(set(Point80).difference(set(Point90)))
print("OnlyScore80: ", OnlyScore80, N)
print("Point90: ", Point90, N)
print("MVP: ", MVP, N)


# print("Lowest90 = ", Lowest90)
# print("OneYuan = ", OneYuan, N)
#为了提高速度可以整合这两个函数，把获取历史数据的放在这个文件里，两个函数只做数值的比较；
#查看一下效率是否高些；
#当一个函数返回多个值时，这么换行接受；
# OnlyScore80 = list(set(Point80).difference(set(Point90)))
# OnlyScore90 = list(set(Point90).difference(set(Point95)))

# print("OnlyScore80: ", OnlyScore80)
# print("OnlyScore90: ", OnlyScore90)
# print("OnlyScore95: ", Point95, N)

# thisToday = ts.get_realtime_quotes('601608')
# openToday = thisToday['open'][0]
# priceToday = thisToday['price'][0]
# print("null", openToday, priceToday)
# IncreaseToday = []
# MVP = []
# for number in Point80:
#     try:
#         thisYesterday = ts.get_hist_data(number)
#         closeYesterday = thisYesterday['close'][0]
#         openYesterday = thisYesterday['open'][0]
#         highYesterday = thisYesterday['high'][0]
#         closeBeforeY = thisYesterday['close'][1]
#         openBeforeY = thisYesterday['open'][1]
#         thisToday = ts.get_realtime_quotes(number)
#         openToday = thisToday['open'][0]
#         priceToday = thisToday['price'][0]
#         lowToday = thisToday['low'][0]
#         openTodayValue = float(openToday)
#         priceTodayValue = float(priceToday)
#         lowTodayValue = float(lowToday)
#         print(111)
#         if openTodayValue >= closeYesterday and lowTodayValue > openYesterday:
#             IncreaseToday.append(number)
#             print(222)
#             print(IncreaseToday)
#
#             if priceTodayValue >= 1.01*closeYesterday:
#                 print(333)
#                 MVP.append(number)
#                 print(MVP)
#     except:
#         continue
# print("Point80: ", Point80, N)
# print("IncreaseToday: ", IncreaseToday)
# print("MVP: ", MVP)
