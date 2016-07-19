# -*- coding: utf-8 -*-

def func(a, *args, **kwargs):
    print a
    print args
    print kwargs.get('type', 'yes')

func(1, 2, 3, 4, name='xiong', age=18)
