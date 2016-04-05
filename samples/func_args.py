# -*- coding: utf-8 -*-

# 必选参数>默认参数
def power(x, n=2):
    res =1;
    while n>0:
        res = res*x
        n = n-1
    return res
# 可变参数
def varargs(age, *args):
    return args
# 关键字参数
def kwargs(age, sex='female',  **kw):
    return kw
# 参数组合
def func(required , default='默认', *args, **kw):
    print '组合参数:required =', required,'default =', default, 'args =', args, 'kw =', kw

if __name__ == '__main__':
    print power(5, 3)
    print varargs(*[1,3,3,4,8])
    print kwargs(30, name='xiong', sex='male')
    func('必选',4,5,6, count=4, age=30)
