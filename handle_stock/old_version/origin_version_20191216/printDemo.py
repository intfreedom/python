import time
import tushare as ts

print(time.strftime('%Y%m%d %H:%M:%S'))
print(3)
ts.get_hist_data('601608')
