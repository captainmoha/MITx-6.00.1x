def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    # Your code here
    seen = {} # dict (value, key)
    result = set() # keys with unique values
    for k,v in aDict.iteritems():
        if v in seen:
            result.discard(seen[v])
        else:
            seen[v] = k
            result.add(k)
    result = list(result)
    result.sort()
    return result
