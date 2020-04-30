# 封装处于低谷的
import datetime
import tushare as ts


def get_lowest(code, start_time='2018-01-01', distance=10, rate_distance=1.02, rate_distance_week=1.01):

    date_today = datetime.datetime.today().strftime('%Y-%m-%d')
    low_value = ''
    
    history = ts.get_hist_data(code, start=start_time)
    low = history['low']
    low_most = low.sort_values().index[0]
    values_low = low[low_most]  # 这里处理最小值的是否有问题，可以同时获得array型数据的最小值及其对应的下标；
    values_now = low[0]

    history_week = ts.get_hist_data(code, ktype='W', start=start_time)
    low_week = history_week['low']
    low_week_most = low_week.sort_values().index[0]
    values_week_low = low_week[low_week_most]
    values_week_now = low_week[0]
    d1 = datetime.datetime.strptime(low_most, '%Y-%m-%d')    # 直接用dateToday不可；类型不一致，
    d2 = datetime.datetime.strptime(date_today, '%Y-%m-%d')  # class 'str'>  class 'datetime.datetime'>

    print("*** values_low, values_now", values_low, values_now, " ***")
    print("*** values_week_low, values_week_now", values_week_low, values_week_now, " ***")
    # print(3, low_most, d1, d2)
    # print(type(d2))
    # print(type(d1))
    day_diff = (d2 - d1).days
    # print(day_diff)
    # //'300423在里是不合理的'调试，这个获取的股票数据都不对；重点关注
    # 用len(low)>Distance, 排除 '603379', '600891', '300767'如这些新股；
    if day_diff < distance or values_now <= rate_distance*values_low or values_week_now <= rate_distance_week*values_week_low:
        low_value = code

    return low_value

