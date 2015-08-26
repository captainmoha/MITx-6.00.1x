# Greatest Common Divisor iteration

# The greatest common divisor of two positive integers is
# the largest integer that divides each of them without remainder.

def gcdIter(a, b):
	current_guess = 0
	gcd = 0
	if a >= b:
		current_guess = b
	else:
		current_guess = a
	while (current_guess > 1):
		if (a % current_guess == 0 and b % current_guess == 0):
			gcd = current_guess
			return gcd
		current_guess -= 1
	gcd = 1
	return gcd

print gcdIter(24, 12)