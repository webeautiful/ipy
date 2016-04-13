# -*- coding: utf-8 -*-

# 内建模块
import datetime
import time
print '--时间处理--'
stime = datetime.datetime.now()
[x*x for x in range(1, 1000)]
etime = datetime.datetime.now()
# 获取时间的毫秒数
print (etime - stime).microseconds

# 获取时间戳
timestamp = int(time.time())
print timestamp

# 将时间戳转换成日期
timeArr = time.localtime(timestamp)
print time.strftime('%Y-%m-%d %H:%M:%S', timeArr)

# 将带毫米的日期格式化为常用日期
withMs = datetime.datetime.now()
print withMs.strftime('%Y-%m-%d %H:%M:%S')
