# -*- coding: utf-8 -*-

# 生成器(保存的是算法)
def odd(s,e):
    seq = range(s,e)
    for n in seq:
        if n % 2 != 0:
            yield n
            print 'after'

if __name__ == '__main__':
    g = (x for x in range(10) if x % 2 != 0)
    for x in g:
        print x
    g2 = odd(10, 20)
    for x in g2:
        print x
