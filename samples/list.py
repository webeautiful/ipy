# -*- coding: utf-8 -*-

if __name__ == '__main__':
    seq = range(100);
    seq.pop(0)
    print seq[::4]
    for i in [2, 5, 7, 8]:
        print i
    print '--列表推导(List Comprehensions)，带条件判断--'
    print [x*x for x in range(1, 100) if x%2 == 0]
