# -*- coding=utf-8 -*-
import itertools
# count 创建无限的迭代器，在for中根本停不下来
natuals = itertools.count(1)
# for  n  in natuals:
#     print(n)
# takewhile 根据条件来控制序列
ns = itertools.takewhile(lambda x:x<=10,natuals
	)
print(list(ns))

# cs = itertools.cycle('ABC')
# #cycle 把传入的序列无限重复，字符串也是序列的一种
# for  c in cs:
#     print(c)



ns = itertools.repeat('A',3)
#repeat 把一个元素无限重复，除非有第2个参数限定重复次数
for n in ns:
    print(n)


# chain() 可以把一组迭代对象串联起来
for c in itertools.chain('ABC','XYZ'):
    print(c)

# groupby() 把迭代器中相邻的重复元素挑出来放在一起
for key,group in itertools.groupby('AAABBCCAAAEEEDADE'):
    print(key,list(group))