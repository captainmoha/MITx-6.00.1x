# find the log iteritavely
def myLog(x, b):
    ans = 1
    if x == b:
    	return ans
    while b ** ans <= x :
        ans += 1
    if b ** ans == x:
    	return ans
    # if the number is not exactly equal to b**ans
    else:
    	return ans - 1



# find the log recursively with a global variable 
ans = 1
def myLog(x, b):
    global ans
    # base cases
    if x == b or x/b == 1 or b ** ans > x:
        return ans
    else:
        ans +=1
        return myLog(x/b, b) 
# tests		
print myLog(51, 6)  # 2
print myLog(122, 5)  # 2
print myLog(120, 4)

# log recursively without a global variable : better solution
def myLog(x, b):
	# base case
	# if the base is greater than x return 0
    if (b > x): 
        return 0
    # recursive step
    # other wise return 1 and add it to the call of myLog 
    #  but this time passing x/b as x
    # this method divides the number by the base until the result
    #  is 1. and the result of this is the number of times 
    #  function was called
    else: 
        return 1 + myLog(x/b, b)