# factorial with recursion 

def recurFact(n):
	if n == 0:
		return 1    # handling zero factorial
	if n == 1:      # base case
		return n
	return n * recurFact(n-1)     # recursive step


print recurFact(5)