#!/usr/bin/env python3

#pickle模块是python的序列化模块，可以用来为任意对象进行序列化和反序列话
#此外，需要注意的一点就是全局变量的使用：
#	在局部范围内(子函数)使用全局变量，必须加global前缀声明，
#	否则创建的就是一个覆盖全局变量的局部变量

import pickle

file_path_A = '/tmp/fileA'
file_path_B = '/tmp/fileB'
pos = 0

def fib_1():
	f = open(file_path_A, 'wb+');
	if f == 0:
		print("open file ", file_path_A)
	f.write(b"This is line 1\n")
	f.write(b"This is line 2\n")
	f.write(b"This is line 3\n")
	f.write(b"This is line 4\n") 
	global pos
	pos = f.tell()
	dir_A = {"name":"Guzheng", "Sex":"male", "Age":18}
	print('At pos {0}, packle the object dir_A:{1}\n'.format(pos, dir_A))
	pickle.dump(dir_A, f)
	f.close()

def fib_2():
	with open(file_path_B, 'wb') as f_b:
		with open(file_path_A, 'rb') as f_a:
			global pos
			f_a.seek(pos, 0)
			print('pos is {0}, file pos is {1}'.format(pos, f_a.tell()))
			x = pickle.load(f_a)
			print("Succeed unpackling dirA:{0} form file {1}".format(x, file_path_A))
			f_b.seek(0, 0)
			pickle.dump(x, f_b)
		f_a.close()
	f_b.close()
def fib_3():
	with open(file_path_B, 'rb') as f:
		f.seek(0, 0)
		dir_A = pickle.load(f)
		print(dir_A)
	f.close()
if __name__ == "__main__":
	import sys
	fib_1()
	fib_2()
	fib_3()
