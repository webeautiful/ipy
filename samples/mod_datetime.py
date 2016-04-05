# -*- coding: utf-8 -*-

import datetime
print '时间处理'
stime = datetime.datetime.now()
[x*x for x in range(1, 1000)]
etime = datetime.datetime.now()
print (etime - stime).microseconds
