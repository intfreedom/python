# -*- coding:utf-8 -*-
#！/user/bin/python3

industry_list = [
  {
     "parent_ind": "女装",
     "name": "连衣裙"
  },
  {
     "name": "女装"
  },
  {
     "parent_ind": "女装",
     "name": "半身裙"
  },
  {
     "parent_ind": "女装",
     "name": "A字裙"
  },
  {
     "name": "数码"
  },
  {
    "parent_ind": "数码",
    "name": "电脑配件"
  },
  {
    "parent_ind": "电脑配件",
    "name": "内存"
  },
]

parent_ind_list = []
name_list = []
for d in industry_list:
    if "parent_ind" in d:
        parent_ind_list.append(d["parent_ind"])
        name_list.append(d["name"])
    else:
        parent_ind_list.append(d["name"])
# parent_ind_list, name_list分别去重
parent_ind_list = list(set(parent_ind_list))
name_list = list(set(name_list))
# parent_ind_list中去掉和name_list重复的部分，就是顶级索引
first_index = [x for x in parent_ind_list if x not in name_list]

# 处理结果的列表
covert_dic = {}


# 转换函数
def convert_format(data):
    try:
        for d in data:
            if "parent_ind" in d and d["parent_ind"] in first_index and "name" in d:       
                covert_dic[d["parent_ind"]] = {d["name"]:{}}
        for d1 in data:
            if "parent_ind" in d1 and d1["parent_ind"] in list(covert_dic.keys()):
                second = covert_dic[d1["parent_ind"]]
                second[d1["name"]] = {}
        for d2 in data:
            for n in covert_dic.values():
                if "parent_ind" in d2 and d2["parent_ind"] in list(n.keys()):
                    n[d2["parent_ind"]] = {d2["name"]:{}}
    except KeyError as e:
        print(e)
    
    return covert_dic
 

if __name__ == '__main__':
    dic = convert_format(industry_list)
    print("result", dic)


# {
#   "数码": {
#     "电脑配件": {
#         "内存" : {}
#      }
#   },
#   "女装" : {
#      "连衣裙": {},
#     "半身裙": {},
#     "A字裙": {}
#   }
# }
