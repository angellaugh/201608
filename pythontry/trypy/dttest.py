# -*- coding:utf-8 -*-
# timedelta 用来做计算
# timestamp  时间戳
# epoch 新时间，新纪元  epochtime=1970年1月1日

from datetime import datetime,timedelta

now = datetime.now()
print(now + timedelta(days = 2,hours = 13));


import hashlib
# 哈希算法

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib'.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())


sha1 = hashlib.sha1()
sha1.update('how to use sha1 in'.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())