import pandas
import matplotlib
import mpl_finance    # inside matplotlib.finance
import matplotlib.pyplot as plt
import csv
import tushare
import datetime
import os
import tushare as ts
# 把这个封装成一个类，然后AAA可以调用，看其筛选出来的股票是否有处于最低值；

def getCode(fileName):
    with open('D:\\Users\\Administrator\\'+fileName+'.csv', 'r', encoding='UTF-8') as f:
        reader = csv.reader(f)
        column = [row[0] for row in reader]
        return column

def GetLowest(startT='2018-01-01',Distance=20,SmallValues=3):
    dateToday = datetime.datetime.today().strftime('%Y-%m-%d')
    column = getCode('Anaconda3' + dateToday)
    i = 1
    L = []
    LNumber = []
    Lowest90 = []
    OneYuan = []  # 记录一元的；
    TwoYuan = []
    # 要取每天最低价里的历史最低价；
    # >>> type(ts.get_hist_data("601608")["low"])
    # <class 'pandas.core.series.Series'>
    # 搞清楚它是什么类型数据，然后处理，,sort_index()和sort_values()可以排序；
    # a1=ts.get_hist_data("601608")["low"].sort_values().index[0]
    # a2=ts.get_hist_data("601608")["low"].sort_values().index[1]
    # d1=datetime.datetime.strptime(a1,'%Y-%m-%d')
    # d2=datetime.datetime.strptime(a2,'%Y-%m-%d')
    # (d2-d1).days
    while i < len(column):
        try:
            # 查询这个hist的默认日期，看是否可以控制日期；控制在一年以内；或者更短；
            # start='2018-01-01'
            history = ts.get_hist_data(column[i], start=startT)
            op = history['open']
            close = history['close']
            low = history['low']
            # error = ts.get_hist_data("300423")['low']这一个是错的，这是为啥
            # 已经有两个票是20181019最低点发起；600794，300158
            k = 0
            number = 0
            # 获取历史最低价，然后得到相减的时间；
            print(1, column[i], low)
            print(len(low))
            # a1=low.sort_values().index[0]
            # a1 = ts.get_hist_data(column[i])['low'].sort_values().index[0]
            a1 = low.sort_values().index[0]
            print(2, a1)
            # 查看此处代码可在命令行运行，但在.py文件中无法运行
            d1 = datetime.datetime.strptime(a1, '%Y-%m-%d')
            d2 = datetime.datetime.strptime(dateToday, '%Y-%m-%d')  # 此处直接用dateToday不可；
            valuesLow = low[a1]
            valuesNow = low[0]
            print("2可以记录最低值", valuesLow, valuesNow)

            if (valuesLow <= (SmallValues-1) and valuesNow <= SmallValues):
                OneYuan.append(column[i])
                # TwoYuan.append(column[i])

            print(3, a1, d1, d2)
            print(type(d2))
            print(type(d1))
            # class 'str'>
            # class 'datetime.datetime'>
            DayDiff = (d2 - d1).days
            print(DayDiff)
            # //'300423在里是不合理的'调试，这个获取的股票数据都不对；重点关注
            #         这是<10的结果['300768', '300423', '600891', '300176']
            # [1, 55, 3462, 3588] 3612
            # 排除 '603379', '600891', '300767'如这些新股；
            if ((DayDiff < Distance or valuesLow / valuesNow >= 0.9) and len(low) > Distance):
                print(5)
                print(i)
                Lowest90.append(column[i])
                print(i)
                LNumber.append(i)

            i += 1
            print("Lowest90", Lowest90)
            print("OneYuan=", OneYuan)
            # print(TwoYuan)
            print(LNumber, i)

        except:
            i += 1
            continue