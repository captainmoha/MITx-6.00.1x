# using functions as first class objects

# apply to each function takes a function and applies
# it to a list

lista = [1,2,3,4,5]
listb = [6,1,2,7,9]
def applyToEach(L,recurFact):
    for i in range(len(L)):
        L[i] = recurFact(L[i])
    return L

# factorial with recursion 

def recurFact(n):
    if n == 0:
        return 1    # handling zero factorial
    if n == 1:      # base case
        return n
    return n * recurFact(n-1)     # recursive step

lista = [1,2,3,4,5]
listb = [6,1,2,7,9]
print applyToEach(lista,recurFact)
x = map(max,lista,listb)
print "mapping list to min " + str(x)
