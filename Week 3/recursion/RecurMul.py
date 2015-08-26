# muliplying with recursion

def recurMul(a, b):
	if b == 1:   # base case
		return a
	else:
		return a + recurMul(a, b-1)  # recursive step

print recurMul(3,7)