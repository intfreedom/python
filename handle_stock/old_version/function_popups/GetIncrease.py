import tushare as ts
ts.set_token('5823bf7ec54e45e3c9845d83a30e5716b08dc6f0b9ef59ea123a92a4')
pro = ts.pro_api()
# # df = pro.daily(ts_code='601608', start_date='20180701', end_date='20180718')
df = pro.daily(ts_code='000009.SZ', start_date='20180701', end_date='20190424')
df1 = pro.daily(ts_code='601608.SH', adj='qfq', start_date='20180101')
print(df1)
print(df)
#查询当前所有正常上市交易的股票列表
data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
print(data)
# print(data['ts_code'][0])
for i in data['ts_code']:
    print(i)
    print(pro.daily(ts_code=i, start_date='20180701', end_date='20190424'))
# 有限制；
# [142 rows x 11 columns]
# 000982.SZ
# Traceback (most recent call last):
#   File "GetIncrease.py", line 15, in <module>
#     print(pro.daily(ts_code=i, start_date='20180701', end_date='20190424'))
#   File "D:\Users\Administrator\Anaconda3\lib\site-packages\tushare\pro\client.py", line 43, in query
#     raise Exception(result['msg'])
# Exception: 抱歉，您每分钟最多访问该接口200次，权限的具体详情访问：https://tushare.pro/document/1?doc_id=108。

# 新股要获取后缀这一点真是烦啊
def continuous(ticket, growthRate = 0.02, opentVSclosey = 0.98):
    # dateToday = datetime.datetime.today().strftime('%Y-%m-%d')
    # Notice: the value of two function is not same, get_hist_data, get_realtime_quotes
    Point80 = ''
    Point90 = ''
    Point95 = ''

    history = ts.get_hist_data(ticket)
    op = history['open']
    close = history['close']
    low = history['low']
    thisYesterday = ts.get_hist_data(ticket)
    closeYesterday = thisYesterday['close'][0]
    openYesterday = thisYesterday['open'][0]
    highYesterday = thisYesterday['high'][0]
    closeBeforeY = thisYesterday['close'][1]
    openBeforeY = thisYesterday['open'][1]
    thisToday = ts.get_realtime_quotes(ticket)
    openToday = thisToday['open'][0]
    priceToday = thisToday['price'][0]
    lowToday = thisToday['low'][0]
    openTodayValue = float(openToday)
    priceTodayValue = float(priceToday)
    lowTodayValue = float(lowToday)

    if (close[0] - op[0]) / op[0] >= growthRate or (low[0] > close[1] and low[0] > op[1]):
        if openTodayValue / closeYesterday >= opentVSclosey and lowTodayValue >= openYesterday:
            Point80 = ticket
            if lowTodayValue >= closeYesterday and (closeBeforeY - openBeforeY) / openBeforeY >= 0.01:
                Point90 = ticket
                if lowTodayValue > highYesterday:
                    Point95 = ticket

    return Point80, Point90, Point95
