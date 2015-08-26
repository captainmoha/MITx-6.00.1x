# sum of the digits of a given number using recursion

# Hint: Mod (%) by 10 gives you the rightmost digit (126 % 10 is 6),
#  while doing integer division by 10 removes the rightmost digit
#  (126 / 10 is 12).

def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    # base case 
    # second operand to make sure that N returns only if 
    #  the length of the string is 1. to prevent premature halting
    #  when N has a zero in it like 566100 or 52044 for example
    if (N % 10 == 0) and (len(str(N))) == 1:
        return N
    # recursive step
    # return the last digit in the number then slice it and pass
    #  the sliced number to the function again until there is only
    #  one digit left
    else:
        return N % 10 + sumDigits(N / 10)
print sumDigits(21640) # 13