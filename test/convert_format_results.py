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

  {
    "parent_ind": "电脑配件",
    "name": "测试"
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

print(parent_ind_list)
print(name_list)
print("first_index", first_index)



covert_dic = {}
values_covert_dic = covert_dic.values()

class AutoVivification(dict):
    """Implementation of perl's autovivification feature."""
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value

# covert_dic = {}
# 转换函数
def convert_format(data):
    # try:
    for d in data:
        if "parent_ind" in d and d["parent_ind"] in first_index and "name" in d:       
            covert_dic[d["parent_ind"]] = {d["name"]:{}}

    for d1 in data:
        if "parent_ind" in d1 and d1["parent_ind"] in list(covert_dic.keys()):
            second = covert_dic[d1["parent_ind"]]
            second[d1["name"]] = {}

    for d2 in data:
        print("covert_dic.values", covert_dic.values())
        # if "parent_ind" in d2 and d2["parent_ind"] in list(n.keys()):
        for n in covert_dic.values():
            print("n", n)
            print("n.keys().list", list(n.keys()))
            if "parent_ind" in d2 and d2["parent_ind"] in list(n.keys()):
                n[d2["parent_ind"]] = {d2["name"]:{}}
                pass
    
    #     for n1 in covert_dic.values():
    #         if "parent_ind" in d2 and d2["parent_ind"] in list(n1.keys()):
    #             third = n1[d2["parent_ind"]]
    #             third[d2["name"]] = {}
    #             pass


            # covert_dic["parent_ind"].setdefault(d1["name"], {})

            # covert_dic[d["parent_ind"]] = {}.fromkeys(d["name"])

                # for d_x in data:
                #     print("test", d_x)
                #     if "parent_ind" in d_x and (d_x["parent_ind"] == d["name"]) and "name" in d_x:
                #         covert_dic[d["parent_ind"]][d["name"]][d_x["name"]] = {}
                #         print("covert_dic", covert_dic)
                #     elif "parent_ind" in d_x and d_x["parent_ind"] == d["name"] and "name" not in d_x:
                #         covert_dic[d["parent_ind"]][d["name"]] = {}
                    
            # elif "parent_ind" in d and d["parent_ind"] in first_index and "name" not in d:
            #     covert_dic[d["parent_ind"]] = {}
            # elif "parent_ind" not in d:
            #     covert_dic[d["name"]] = {}
    # except:
    # KeyError: 'parent_ind'
        # pass
    return covert_dic
 


        


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

if __name__ == '__main__':
    print("3?")
    dic = convert_format(industry_list)
    print("result", dic)
    print("covert_", covert_dic)
    print("values", values_covert_dic)

