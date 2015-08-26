
def iterPower(base, exp):
	int(exp)
	result = 1
	while exp > 0:
		result *= base
		exp -= 1
		pass
	return result

print iterPower(2,8)