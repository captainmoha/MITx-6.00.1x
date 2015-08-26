def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    # Your function implementation here
    #l = [] 
    for i in range(len(L)):
        #print i
        #print "Length of L now" + str(len(L))
        try:
            if not f(L[i]):
                L.remove(L[i])
        except IndexError:
            try:
                i -= 1
                if not f(L[i]):
                    L.remove(L[i])
            except IndexError:
                i -= 1
                if not f(L[i]):
                    L.remove(L[i])
    #print str(L) + " inside satisfiesF"
    return len(L)
run_satisfiesF(L, satisfiesF)