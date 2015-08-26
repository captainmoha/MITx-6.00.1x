# recursion week 3 

def iterMul(a,b):
	result = 0

	while b > 0:
		result += a
		b -= 1
		pass
	return result

print iterMul(9,1)