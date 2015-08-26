def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float; base^exp
    '''
    # Your code here
    float(base)
    # base case
    if exp <= 0:
        return 1
    # if power is even 
    elif exp % 2 == 0:
        return recurPowerNew(base * base, exp / 2)
    # if power is odd
    return base * recurPowerNew(base, exp - 1)

print recurPowerNew(3,3)
print recurPowerNew(3,4)