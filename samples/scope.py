# -*- coding: utf-8 -*-

def outerFunc():
    var = 'global'
    def func():
        var = var+'local'
        return var
    return func()

print outerFunc()
