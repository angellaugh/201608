# -*- coding: utf-8 -*-
# 利用递归函数计算阶乘
# N!=1*2*3*4*5...*N
# def fact(n):
# 	if n == 1:
# 		return 1
# 	return n * fact(n-1)
# print('fact(1)=',fact(1))
# print('fact(5)=',fact(5))
# print('fact(10)=',fact(10))

# # 利用递归函数移动汉诺塔：
# def move(n,a,b,c):
#     if n == 1:
#     	print('move',a,'-->',c)
#     	return
#     move(n-1,a,c,b)
#     print('move',a,'-->',c)
#     move(n-1,b,a,c)

# move(4,'A','B','C')


# generator 生成器创建表达式
# g = (x * x for x in range(10))
# for n in g:
#     print(n)
# generator 写 斐波拉契数列

def fib(max):
	n,a,b = 0,0,1
	while n<max:
		print(b)
		a,b = b,a+b
		n = n + 1;
	return 'done';

fib(7)


s = (x * x for x in range(5))
for  x  in s:
	print(x);


from collections import Iterator
print(isinstance((x for x in range(10)),Iterator));


from functools import reduce
def sss(x,y):
	return x + y

print(reduce(sss,[1,3,5,7,9]))


