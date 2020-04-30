# 此处去掉st和新的；
import csv
import re


def filter_code_new(ticket, ticket_day, ticket_new_limit=88, condition=r'[688]'):
    if ticket_day > ticket_new_limit and (not re.match(condition, ticket)):    # re.match()若匹配成功返回一个Match对象，否则返回None
            return True
    else:
        return False


def filter_code_st(ticket_re_name, condition=r'[*stST]'):
    if not re.match(condition, ticket_re_name):  # re.match()若匹配成功返回一个Match对象，否则返回None
            return True
    else:
        return False


def save_code(file_name, tickers_list):
    with open(r'./Data/' + file_name + '.csv', 'w', encoding='UTF-8') as f:
        # 加上\n就不会报错，
        for i in tickers_list:
            f.write(i + '\n')  # Terminate lines with \n 使用\ n终止行


def get_code(file_name):
    with open(r'./Data/' + file_name + '.csv', 'r', encoding='UTF-8') as f:
        reader = csv.reader(f)
        column = [row[0] for row in reader]
        return column

