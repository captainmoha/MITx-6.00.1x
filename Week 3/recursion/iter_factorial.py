# get the factorial using iteration 
def iterFact(a):
	result = 1
	if a == 0:
		result = 1
	while a > 0:
		result *= a
		a -= 1
		
	return result
	
print iterFact(5)
