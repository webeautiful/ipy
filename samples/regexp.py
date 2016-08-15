# -*- coding: utf-8 -*-
import re

kw_list = ['sexy', '民粹', '反动']
kw_str = '|'.join(kw_list)
pattern = re.compile(r'%s'%kw_str)
print pattern.search('全球经济的不景气，导致民粹主义抬头').group()
