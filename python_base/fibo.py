#/usr/bin/env python3
def fib_1(n):
	a, b = 0, 1
	while b < n:
		print(b,' ')
		a, b = b, a+b
	print()

def fib_2(n):
	result = []
	a, b = 0, 1
	while b < n:
		result.append(b)
		a, b = b, a+b
	return result
if __name__ == "__main__":
	import sys
	fib_1(int(sys.argv[1]))
	fib_2(int(sys.argv[1]))
