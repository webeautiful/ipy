# -*- coding: utf-8 -*-
from ConfigParser import ConfigParser, SafeConfigParser
conf_file = 'test.conf'

# 读取配置文件
cf = ConfigParser()
cf.read(conf_file)
print cf

# 列出所有的section
secs = cf.sections()
print secs

# 返回某个section下，所有key组成的列表
opts = cf.options('sec_a')
print opts

# 返回某个section下，所有key/value组成的tupleList
kvs = cf.items('sec_a')
print kvs

# 返回某个section下，某个key的值
int_val = cf.getint('sec_b', 'b_key1')
str_val = cf.get('sec_b', 'b_key2')
print int_val
print str_val

url = cf.get('portal', 'url')
print url

scf = SafeConfigParser()
scf.read(conf_file)
print scf.get('portal', 'url')
'''
# write config
# 创建/更新某个key值
cf.set('sec_b', 'b_key3', 'updated+$r')
# 创建新的section
cf.add_section('new_sec')
cf.set('new_sec', 'new_key', 'new_value')

with open(conf_file, 'wb') as f:
    cf.write(f)
'''
