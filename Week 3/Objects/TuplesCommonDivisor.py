# tupels lecture
# common divisors
def findDivisors(n1, n2):
	divisors = ()

	for i in range(1, min(n1,n2) + 1): 
		if (n1 % i == 0) and (n2 % i == 0):
			divisors += (i,)
	return divisors

print findDivisors(20,100)

divs = findDivisors(20,100)
# get the total of the common divisors of the given two numbers
total = 0 
for i in divs:
	total += i
print total