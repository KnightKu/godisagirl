#!/usr/bin/env python3

#自定义的异常类型都要从异常基类Exception派生
class MyError(Exception):
	#重写__init__解析函数
	def __init__(self, value):
		self.value = value
	#重写__str__方法，让异常可打印
	def __str__(self):
		return repr(self.value)
	

def test1(x, y):
	try:
		result = x/y
	except (ZeroDivisionError):
		print("division by zero!\n")
	else:
		print("result is {0}\n".format(result))
	finally:
		print("excuteing finally cluse!\n")

def test2():
	try:
		#手动触发一个自定义的异常
		raise MyError(12*12)
	except MyError as e:
		print('My exception occurred, value:', e.value)

def test3():
	try:
		#用Exception()函数创建一个匿名的异常示例
		raise Exception('Spam', 'Eggs')
	except Exception as inst:
		print(type(inst))
		print(inst.args)
		print(inst)
		x, y = inst.args
		print('x = ', x)
		print('y = ', y)

if __name__ == '__main__':
	test1(2, 3)
	test1(3, 0)
	test2()
	test3()
