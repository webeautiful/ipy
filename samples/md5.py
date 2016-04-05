# -*- coding: utf-8 -*-

import hashlib

def md5(str):
    obj = hashlib.md5()
    obj.update(str)
    md5Str = obj.hexdigest()
    return md5Str

print md5('8888')[0:2]
