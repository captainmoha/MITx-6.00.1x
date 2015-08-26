
def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    # base case
    # if string is empty then length is zero
    if aStr == '':
        
        return 0
    # recursive step
    # add 1 + recall the function again with a string that is less by one
    #  charchter after slicing it away
    else:
        return 1 + lenRecur(aStr[1:])
        

