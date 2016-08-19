# -*- coding: utf-8 -*-
# print('hello,world');

# print('100+200=',100+200);

# name = input('please input your name:');

# print('hello',name);

# a = 100
# if a>=0:
#     print(a)
# else:
# 	print(-a)


# s = 'Python-中文'
# print(s)
# b = s.encode('utf-8')
# print(b)
# print(b.decode('utf-8'))

# s = input('birth:')
# birth = int(s)
# if birth<2000:
# 	print('00前')
# else:
# 	print('00后');

# # 注意:
# # input()返回的是字符串
# # 必须通过int()将字符串转换为整数
# # 才能用于数值比较:
# age = int(input('Input your age: '))

# if age >= 18:
#     print('adult')
# elif age >= 6:
#     print('teenager')
# else:
#     print('kid')


# salary
# salary = int(input('Your salary:'))
# if salary >= 10000:
#     print('cool~')
# elif salary >= 5000:
#     print('ok')
# else:
# 	print('sadly!');

# names = ['henry','annie','elieen']
# for name in names:
# 	print(name);

# sum = 0
# for x in[1,2,3,4,5,6,7,8,9,10]:
#     sum = sum + x
# print(sum);

# sum = 0
# for x in range(101):
#     sum = sum + x
# print(sum);

# sum3 = 0
# n = 99
# while n>0:
# 	sum = sum + n
# 	n = n-2
# print(sum);

# L = ['Bart','Lisa','Adam']

# for x in L:
# 	print('Hello,'+x);

# acc = 1
# n = 1
# while n<=100:
# 	acc = acc * n
# 	n = n+1
# print(acc);

# d.get('wahaha');

d = {'henry':95,'bob':80,'annie':70}
print('d[\'henry\']=',d['henry']);
print('d[\'bob\']=',d['bob']);
print('d[\'annie\']=',d['annie']);
print('d.get(\'waha\',-1)=',d.get('waha',-1));