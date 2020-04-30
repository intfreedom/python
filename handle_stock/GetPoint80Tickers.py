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


# 此处去掉st和新的；
def filterCode(ticker, tickerDay):
    if tickerDay > 20:
        tickerReName = ts.get_realtime_quotes(ticker)['name'][0]
        if re.match(r'[*stST]', tickerReName) == None:# re.match()若匹配成功返回一个Match对象，否则返回None
            return True


def getPointTicker(ticker, growthRate=0.01, startT='2018-01-01'):
    tickerName = ''
    tickerContinusName = ''
    history = ts.get_hist_data(ticker)
    op = history['open']
    close = history['close']
    Week = ts.get_hist_data(ticker, ktype='W', start=startT)
    WeekOpen = Week['open'][0]
    WeekClose = Week['close'][0]
    print("why , here1111")
    # I think this one, can be, (close[0]>close[1] or open[0]>close[1] or hi>close[1]) and close[0]>op[0]
    # (close[0] - op[0]) / op[0] >= 1% and close[0] > close[1] the final
    if (close[0] - op[0]) / op[0] >= growthRate and (close[0] > close[1]):
        print("why , here222221")
        if(filterCode(ticker, len(op))):
            print("why , here33333")
            tickerName = ticker
            if (close[1] - op[1]) / op[1] >= growthRate or WeekClose >= 1.008*WeekOpen:
                tickerContinusName = ticker

    return tickerName, tickerContinusName


def saveCode(fileName, tickersList):
    with open(r'./Data/'+fileName+'.csv', 'w', encoding='UTF-8') as f:
        # 加上\n就不会报错，
        for i in tickersList:
            f.write(i + '\n')  # Terminate lines with \n 使用\ n终止行


def getCode(fileName):
    with open(r'./Data/'+fileName+'.csv', 'r', encoding='UTF-8') as f:
        reader = csv.reader(f)
        column = [row[0] for row in reader]
        return column


def GetLowest(ticket, startT='2018-01-01',Distance = 30, rateDistance=1.08):
    dateToday = datetime.datetime.today().strftime('%Y-%m-%d')
    lowVaule = ''
    history = ts.get_hist_data(ticket, start=startT)
    low = history['low']
    # error = ts.get_hist_data("300423")['low']这一个是错的，这是为啥
    # 已经有两个票是20181019最低点发起；600794，300158
    # 获取历史最低价，然后得到相减的时间；
    print(1, ticket, low)
    print(len(low))
    # a1=low.sort_values().index[0]
    # a1 = ts.get_hist_data(column[i])['low'].sort_values().index[0]
    a1 = low.sort_values().index[0]
    print(2, a1)
    d1 = datetime.datetime.strptime(a1, '%Y-%m-%d')
    d2 = datetime.datetime.strptime(dateToday, '%Y-%m-%d')
    # 此处直接用dateToday不可；类型不一致，# class 'str'>   # class 'datetime.datetime'>
    # 简化，简化，简化；“300623”，值不对了，有问题；
    valuesLow = low[a1]   # 这里处理最小值的是否有问题，可以同时获得array型数据的最小值及其对应的下标；
    valuesNow = low[0]
    print("2可以记录最低值", valuesLow, valuesNow)
    print(3, a1, d1, d2)
    print(type(d2))
    print(type(d1))
    DayDiff = (d2 - d1).days
    print(DayDiff)
    # //'300423在里是不合理的'调试，这个获取的股票数据都不对；重点关注
    # 用len(low)>Distance, 排除 '603379', '600891', '300767'如这些新股；
    if DayDiff < Distance or valuesNow <= rateDistance*valuesLow:
        lowVaule = ticket
    return lowVaule


TickersFileName = 'AllTickets'
saveCode(TickersFileName, tickers)
column = getCode(TickersFileName)
print(column)
N = 0    # 进度查看
Point80 = []
Point90 = []
for tickerNumber in column:
    try:
        print(111111)
        tickerPoint = getPointTicker(tickerNumber)
        print("*******", tickerPoint)
        if tickerPoint[0] != '':
            Point80.append(tickerNumber)
            tickerLowest = GetLowest(tickerNumber)    # 判断该股票是否是最低点；
             # 判断是否连续增长或周增长   或最低点；
            if tickerPoint[1] != '' or tickerLowest != '':
                Point90.append(tickerNumber)
        print(Point80, N)
        print(Point90, N)
    except:
        continue
    N += 1

fileSavePoint80Name = '00000000-10101000-'+dateToday    # 用于记录历史分析；
saveCode(fileSavePoint80Name, Point80)
fileSavePoint80Fixed = '10101000'    # 用于读取，每次读取一个固定文件；
saveCode(fileSavePoint80Fixed, Point80)
# 这两者的区别就是控制数量；看看差异大小；

fileSavePoint90Name = '00000000-10101000-Point90-'+dateToday    # 用于记录历史分析；
saveCode(fileSavePoint90Name, Point90)
fileSavePoint90Fixed = '10101000-Point90'    # 用于读取，每次读取一个固定文件；
saveCode(fileSavePoint90Fixed, Point90)

