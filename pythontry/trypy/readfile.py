# -*- coding: utf-8 -*-

try:
    f = open('/pythontry/test.txt','r',encoding='gbk',errors='ignore');
    print(f.read());	
finally:
    if f:
        f.close()



from datetime import datetime

with open('test.txt', 'w') as f:
    f.write('今天是 ')
    f.write(datetime.now().strftime('%Y-%m-%d'))

with open('test.txt', 'r') as f:
    s = f.read()
    print('open for read...')
    print(s)

with open('test.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)