
# def area_of_circle(r):
# 	p = 3.14
# 	# r = int(input('input the r:'))
# 	s = p * r * r
# 	# MM = print('面积是：',s);
# 	return s;
# print('input半径：',area_of_circle);
import math;


# def my_abs(x):
# 	if x >= 0:
# 		return x
# 	else:
# 		return -x
def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x;



# n1 = 255
# print(hex(n1));

