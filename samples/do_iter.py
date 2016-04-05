# -*- coding: utf-8 -*-

print """总结:
任何可迭代对象都可以作用于for循环"""

def iter_str(str):
    for char in str.decode('utf-8'):
        print(char)
def iter_tuple(tpl):
    for v in tpl:
        print v
def iter_list(seq):
    for v in seq:
        print v
def iter_dict(d):
    for k in d:
        print k
def iter_dict2(d):
    if isinstance(d, dict):
        tupleList = d.items()
        iterObj = tupleList;
    elif isinstance(d, list):
        kylist = enumerate(d)
        iterObj = kylist
    for k,v in iterObj:
        print 'key =',k,'value =',v

if __name__ == '__main__':
    string = '中国good'
    tpl = ('中国', 'good')
    lst = ['中', '国', 'good']
    d = {'nation': '中国', 'how': 'good'}

    print '--迭代字符串--'
    iter_str(string)
    print '--迭代元组--'
    iter_tuple(tpl)
    print '--迭代序列--'
    iter_list(lst)
    print '--迭代字典--'
    iter_dict(d)
    iter_dict(d.values())
    print '--迭代索引元素对列表--'
    iter_dict2(lst)
    print '--迭代元组列表--'
    iter_dict2(d)
