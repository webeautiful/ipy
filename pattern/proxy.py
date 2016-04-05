# -*- coding: utf-8 -*-

# 代理/装饰模式

def query_count_proxy(fun):
    def wrapper(name, age):
        print 'do something before'
        rv = fun(name, age)
        print 'do something after'
        return rv
    return wrapper

@query_count_proxy
def query_count(name, age):
    print 'name is %s, age is %d' % (name,age)
    return 'name is %s, age is %d' % (name,age)

# query_count = query_count_proxy(query_count)
query_count('Lee', 20)
