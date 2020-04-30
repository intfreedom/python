import tushare
import tushare as ts
import datetime
import os.path
from HandleCode import filter_code_new
from HandleCode import filter_code_st
from HandleCode import get_code
from HandleCode import save_code
from LowestPrice import get_lowest
from OneTwoThree import one_two_three

code_all_data = ts.get_stock_basics()
code = code_all_data.index.tolist()
dateToday = datetime.datetime.today().strftime('%Y-%m-%d')
if not os.path.isdir('Data'):
    os.makedirs('Data')
file = r'./Data/AllTickets'+dateToday+'.csv'
code_all_data.to_csv(file)    # 保存所有信息的文件
column = get_code('AllTickets'+dateToday)
print("<<< AllTickets", column, len(column), " >>>")

N = 0    # 进度查看
Point80 = []
Point90 = []
one_day_lowest = []
two_day_lowest = []
three_days = []
two_day_high = []
two_yuan = []
one_yuan = []

hs_300 = ts.get_hs300s()
hs_300_code = hs_300['code']
print("code", hs_300_code)
for code_number in hs_300_code[1:10]:
    print("code[]", hs_300_code[0], hs_300_code[1], hs_300_code[2], hs_300_code[3], hs_300_code[4], hs_300_code[5])
    start_time = '2018-01-01'
    history = ts.get_hist_data(code_number, start=start_time)
    test = ts.get_realtime_quotes('000050')    # 获取所有沪市的就会有问题；
    try:
        start_time = '2018-01-01'
        history = ts.get_hist_data(code_number, start=start_time)
        history_week = ts.get_hist_data(code_number, ktype='W', start=start_time)
        print("&&&&&&&history", history)
        test = ts.get_today_all(code_number, date=start_time)
        print("&&&&&&&test", test)
        open_value = history['open']
        close = history['close']
        high = history['high']
        low = history['low']
        low_week = history_week['low']

        if filter_code_new(code_number, len(open_value)):
            code_point = one_two_three(code_number, open_value, close, high)
            print("### ", code_point, " ###")

            if code_point[0] != '' and get_lowest(code_number, low, low_week) != '':
                one_day_lowest.append(code_number)
                if 2 <= low[0] <= 3:    # 这种方案，15：09 start
                    two_yuan.append(code_number)
                if low[0] < 2:
                    one_yuan.append(code_number)

            if code_point[1] != '' and get_lowest(code_number, low, low_week) != '':
                two_day_lowest.append(code_number)

            if code_point[2] != '':
                three_days.append(code_number)

            if code_point[3] != '':
                two_day_high.append(code_number)
    except:
        continue

    N += 1
    print("<<< one_yuan", one_yuan, len(one_yuan), N, " >>>")
    print("<<< two_yuan", two_yuan, len(two_yuan), N, " >>>")
    print("<<< one_day_lowest", one_day_lowest, len(one_day_lowest), N, " >>>")
    print("<<< two_day_lowest", two_day_lowest, len(two_day_lowest), N, " >>>")
    print("<<< three_days", three_days, len(three_days), N, " >>>")
    print("<<< two_day_high", two_day_high, len(two_day_high), N, " >>>")

file_one_yuan = 'one_yuan_'+dateToday    # 用于记录历史分析；
save_code(file_one_yuan, one_yuan)
file_one_yuan_fixed = 'one_yuan'    # 用于读取，每次读取一个固定文件；
file_address = r'./Data/'
if os.path.exists(file_address+'one_yuan'+'.csv'):    # 其实不必，saveCode的这种写法直接覆盖原文件
    os.remove(file_address+'one_yuan'+'.csv')
save_code(file_one_yuan_fixed, one_yuan)    # 'w' 只能写 覆盖整个文件 不存在则创建
# 这两者的区别就是控制数量；看看差异大小；

file_two_yuan = 'two_yuan_'+dateToday    # 用于记录历史分析；
save_code(file_two_yuan, two_yuan)
file_two_yuan_fixed = 'two_yuan'    # 用于读取，每次读取一个固定文件；
file_address = r'./Data/'
if os.path.exists(file_address+'two_yuan'+'.csv'):    # 其实不必，saveCode的这种写法直接覆盖原文件
    os.remove(file_address+'two_yuan'+'.csv')
save_code(file_two_yuan_fixed, two_yuan)    # 'w' 只能写 覆盖整个文件 不存在则创建
# 这两者的区别就是控制数量；看看差异大小；

file_one_day_lowest = 'one_day_lowest_'+dateToday    # 用于记录历史分析；
save_code(file_one_day_lowest, one_day_lowest)
file_one_day_lowest_fixed = 'one_day_lowest'    # 用于读取，每次读取一个固定文件；
file_address = r'./Data/'
if os.path.exists(file_address+'one_day_lowest'+'.csv'):    # 其实不必，saveCode的这种写法直接覆盖原文件
    os.remove(file_address+'one_day_lowest'+'.csv')
save_code(file_one_day_lowest_fixed, one_day_lowest)    # 'w' 只能写 覆盖整个文件 不存在则创建
# 这两者的区别就是控制数量；看看差异大小；

file_two_day_lowest = 'two_day_lowest_'+dateToday    # 用于记录历史分析；
save_code(file_two_day_lowest, two_day_lowest)
file_two_day_lowest_fixed = 'two_day_lowest'    # 用于读取，每次读取一个固定文件；
file_address = r'./Data/'
if os.path.exists(file_address+'two_day_lowest'+'.csv'):    # 其实不必，saveCode的这种写法直接覆盖原文件
    os.remove(file_address+'two_day_lowest'+'.csv')
save_code(file_two_day_lowest_fixed, two_day_lowest)    # 'w' 只能写 覆盖整个文件 不存在则创建
# 这两者的区别就是控制数量；看看差异大小；

file_three_days = 'three_days_'+dateToday    # 用于记录历史分析；
save_code(file_three_days, three_days)
file_three_days_fixed = 'three_days'    # 用于读取，每次读取一个固定文件；
file_address = r'./Data/'
if os.path.exists(file_address+'three_days'+'.csv'):    # 其实不必，saveCode的这种写法直接覆盖原文件
    os.remove(file_address+'three_days'+'.csv')
save_code(file_three_days_fixed, three_days)    # 'w' 只能写 覆盖整个文件 不存在则创建
# 这两者的区别就是控制数量；看看差异大小；

