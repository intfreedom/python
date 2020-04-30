import tushare
import tushare as ts
import datetime
import os.path
from HandleCode import filter_code_new
from HandleCode import filter_code_st
from HandleCode import get_code
from HandleCode import save_code

code_all_data = tushare.get_stock_basics()
code = code_all_data.index.tolist()
dateToday = datetime.datetime.today().strftime('%Y-%m-%d')
if not os.path.isdir('Data'):
    os.makedirs('Data')
file = r'./Data/AllTickets'+dateToday+'.csv'
code_all_data.to_csv(file)    # 保存所有信息的文件
column = get_code('AllTickets'+dateToday)
print("<<< AllTickets", column, len(column), " >>>")

N = 0    # 进度查看
point_80 = []
point_90 = []

for code_number in column[0:10]:
    try:
        history = ts.get_hist_data(code_number)#默认最近三年的日线数据；
        print("---", type(history),history, "---")
        p_change = history['p_change']
        low = history['low']
        high = history['high']
        code_filter = filter_code_new(code_number, len(low))

        print("<<< ", code_number, low, p_change," >>>")
        print("<<<p_change[0]+low[0:365] ", code_number, p_change[0],low[0:365]," >>>")
        print("<<<min(low[0:30] ", code_number, min(low[0:30]), " >>>")
        print("<<<min(low[0:365] ", code_number, min(low[0:365]), " >>>")
        print("<<<max(high[0:30] ", code_number, max(high[0:30]), " >>>")
        print("<<<max(high[0:365] ", code_number, max(high[0:365]), " >>>")

        high_low = max(high[0:365])/min(low[0:30]) 
        low_low = min(low[0:365])/min(low[0:30])
	#0:365相当于交易日从2020-03-20至2018-09-14,这个跨度接近于一年半，可以覆盖大部分的涨跌区间，代商榷；
	#当最近30天的最低点就是0-365的最低点,low_low==1;否则，那么最近30-365天的最低点小于最近30天的最低点，low_low<1;所以范围是low_low <= 1,这个值越小表示当前股价越高，暂设置为0.8试一试；也就是当前最低点是0-365最低点的1.2倍；
        if code_filter and (high_low >= 3) and (low_low >= 0.9):
            print(code_number,p_change)
            if 2 <= p_change[0] < 5:
                point_80.append(code_number)
            if p_change[0] >= 5:
                point_90.append(code_number)
    except:
        continue

    N += 1
    print("<<< point_80", point_80, len(point_80), N, " >>>")
    print("<<< point_90", point_90, len(point_90), N, " >>>")

file_point_80 = 'point_80_'+dateToday    # 用于记录历史分析；
save_code(file_point_80, point_80)
file_point_80_fixed = 'point_80'    # 用于读取，每次读取一个固定文件；
file_address = r'./Data/'
if os.path.exists(file_address+'point_80'+'.csv'):    #其实不必，saveCode的这种写法直接覆盖原文件
    os.remove(file_address+'point_80'+'.csv')
save_code(file_point_80_fixed, point_80)    # 'w' 只能写 覆盖整个文件 不存在则创建
# 这两者的区别就是控制数量；看看差异大小；

file_point_90 = 'point_90_'+dateToday    # 用于记录历史分析；
save_code(file_point_90, point_90)
file_point_90_fixed = 'point_90'    # 用于读取，每次读取一个固定文件；
file_address = r'./Data/'
if os.path.exists(file_address+'point_90'+'.csv'):    #其实不必，saveCode的这种写法直接覆盖原文件
    os.remove(file_address+'point_90'+'.csv')
save_code(file_point_90_fixed, point_90)    # 'w' 只能写 覆盖整个文件 不存在则创建
# 这两者的区别就是控制数量；看看差异大小；

