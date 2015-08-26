# power using recursion

def recurPower(base, exp):

    # base case if exp == 1 return base
    if exp == 0:
    	return 1
    
    return base * recurPower(base, exp - 1)

print recurPower(2,4)