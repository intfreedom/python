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


# 转换函数
def convert_format(data):
    # 分别存放父，子索引的列表
    parent_ind_list = []
    name_list = []
    for number_dic in data:
        parent_ind_list.append(number_dic["parent_ind"])
        name_list.append(number_dic["name"])

    # 目标数据中最多嵌套三级索引，原父，子索引中重叠的部分即是第二级索引
    second_index = list(set(parent_ind_list).intersection(set(name_list)))
    # 原父索引中去掉重叠部分，即为现第一级索引
    first_index = list(x for x in parent_ind_list if x not in second_index)
    # 原子索引中去掉重叠部分，即为现第三级索引


    covert_dic = {}

    for d in data:
        if d["parent_ind"] in first_index and d.has_key("name"):
            for d_x in data:
                if d_x["parent_ind"] == d["name"] and d_x.has_key("name"):
                    covert_dic[d["parent_ind"]][d["name"]][d_x["name"]] = {}
                elif d_x["parent_ind"] == d["name"] and (!d_x.has_key("name")):
                    covert_dic[d["parent_ind"]][d["name"]] = {}
        elif d["parent_ind"] in first_index and (!d.has_key("name")):
            covert_dic[d["parent_ind"]] = {}
        elif !d.has_key("parent_ind"):
            covert_dic[d["name"]] = {}
   
   for d_second in data:
       if d_second["parent_ind"] in second_index and d_second.has_key("name"):
           for d_covert_dic in covert_dic:
               if d_covert_dic.has_key(d_second["parent_ind"]):
                   
                   
               
             
            

 



    for d_x in data:
        for x_key in covert_dic.keys():
            if x_key != d_x["parent_ind"]:
                if x_key != d_x["name"]:
                    covert_dic[d_x["parent_ind"]] = d_x["name"]
                else:
                    d_x["parent_ind"] = {}[d_x["parent_ind"]]
            else:
                if


        covert_list.append(d_x)
        covert_list[d_x["parent_ind"]] = d_x["name"]

{
  "数码": {
    "电脑配件": {
        "内存" : {}
     }
  },
  "女装" : {
     "连衣裙": {},
    "半身裙": {},
    "A字裙": {}
  }
}