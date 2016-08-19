# -*- coding: utf-8 -*-

import math

# def my_abs(x):
# 	if not isinstance(x,(int,float)):
# 		raise TypeError('bad operand type')
# 	if x >= 0:
# 		return x
# 	else:
# 		return -x
# def move(x,y,step,angle=0):
# 	nx = x + step * math.cos(angle)
# 	ny = y - step * math.sin(angle)
# 	return nx,ny

# n = my_abs(-20)
# print(n)

# x,y=move(100,100,60,math.pi/6)
# print(x,y)

# my_abs('123')


def power(x,n):
	s = 1
	while n>0:
		n = n -1
		s = s * x
	return s
def enroll(name,gender,age=6,city='beijing'):
	print('name:',name)
	print('gender:',gender)
	print('age:',age)
	print('city:',city)

enroll('猪头',13)

def hello(greeting,*args):
	if(len(args)==0):
		print('%s!'%greeting)
	else:
		print('%s,%s!'%(greeting,','.join(args)))
hello('hi')
hello('hi','Sarah')
hello('hi','henry','bob','annie')


names = ('bart','lisa')
hello('hello',*names)


def fact(n):
	return fact_iter(n,1)

def fact_iter(num,product):
	if num == 1:
		return product
	return fact_iter(num -1,num * product)

print(fact(3));


print(fact(100));

# print(fact(1000));
print(fact_iter(20,60))
