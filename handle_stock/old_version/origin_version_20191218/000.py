import csv
import datetime
from AAGetLowestPrice import GetLowest
from AAA import continuous
# 从20180101至今，所有最小值至今差距20天内的，所用低票价在3元以内的；
Lowest90 = []
OneYuan = []
Point80 = []
Point90 = []
Point95 = []

N = 0 #相当于查看进度，一共3600只；
def getCode(fileName):
    with open('D:\\Users\\Administrator\\'+fileName+'.csv', 'r', encoding='UTF-8') as f:
        reader = csv.reader(f)
        column = [row[0] for row in reader]
        return column

dateToday = datetime.datetime.today().strftime('%Y-%m-%d')
column = getCode('Anaconda3' + dateToday)
print(column)

for i in column:
    try:
        ticketL = GetLowest(i)
        if ticketL[1] != '':
            Lowest90.append(ticketL[1])
        if ticketL[0] != '':
            OneYuan.append(ticketL[0])
        print(Lowest90, OneYuan, N)
    except:
        continue

    try:
        ticketC = continuous(i)
        if ticketC[0] != '':
            Point80.append(ticketC[0])
        if ticketC[1] != '':
            Point90.append(ticketC[1])
        if ticketC[2] != '':
            Point95.append(ticketC[2], N)
    except:
        continue

    N += 1

print("Lowest90 = ", Lowest90)
print("OneYuan = ", OneYuan, N)
#为了提高速度可以整合这两个函数，把获取历史数据的放在这个文件里，两个函数只做数值的比较；
#查看一下效率是否高些；
#当一个函数返回多个值时，这么换行接受；
OnlyScore80 = list(set(Point80).difference(set(Point90)))
OnlyScore90 = list(set(Point90).difference(set(Point95)))
print("OnlyScore80: ", OnlyScore80)
print("OnlyScore90: ", OnlyScore90)
print("OnlyScore95: ", Point95, N)
