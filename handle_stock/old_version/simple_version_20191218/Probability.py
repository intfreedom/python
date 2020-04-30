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
# Point80 = []
# Point90 = []
# one_day_lowest = []
# two_day_lowest = []
# three_days = []
# two_day_high = []
# two_yuan = []
# one_yuan = []
one_day_stop = 0
two_day_stop = 0
three_day_stop = 0
two_probability = 0
three_probability = 0

for code_number in column:
    try:
        start_time = '2018-01-01'
        history = ts.get_hist_data(code_number, start=start_time)
        open_value = history['open']
        p_change = history['p_change']

        if filter_code_new(code_number, len(open_value)):
            i = len(p_change)-1
            print("&&&", i, p_change[i], "&&&")

            N += 1
            while i > 0:
                if p_change[i] >= 7:
                    print("***", p_change[i], "***")
                    one_day_stop += 1
                    if p_change[i-1] >= 7:
                        two_day_stop += 1
                        if p_change[i-2] >= 7:
                            three_day_stop += 1
                i -= 1

        two_probability = two_day_stop / one_day_stop*100
        three_probability = three_day_stop / one_day_stop*100

    except:
        continue

print("<<< ", N, one_day_stop, two_day_stop, three_day_stop, two_probability, "%", three_probability, "%", " >>>")
print("<<< ", '%.2f' % two_probability, "%      ", '%.2f' % three_probability, "%", " >>>")


# one_yuan = [dateToday, 'two_probability: ', two_probability, 'three_probability: ', three_probability]    # 用于记录历史分析；
# file_probability_fixed = 'one_yuan'    # 用于读取，每次读取一个固定文件；
# file_address = r'./Data/'
# if os.path.exists(file_address+'one_yuan'+'.csv'):    # 其实不必，saveCode的这种写法直接覆盖原文件
#     os.remove(file_address+'one_yuan'+'.csv')
# save_code(file_probability_fixed, one_yuan)    # 'w' 只能写 覆盖整个文件 不存在则创建
# # 这两者的区别就是控制数量；看看差异大小；