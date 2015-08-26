# fibonacci using recursion

def fib(n):
	assert (type(n) == int) and (n >= 0)
	# base cases
	# there are two base cases girl rabbit is pregnant in the first month
	if (n == 0) or (n == 1):
		return 1

	else:
		return fib(n - 1) + fib(n - 2)


print fib(0)
print fib(1)
print fib(2)
print fib(3)
print fib(4)
