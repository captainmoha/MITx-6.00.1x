# program 1 
def program1(L):
    multiples = []
    for x in L:
        for y in L:
            multiples.append(x*y)
    return multiples

# worst case : 3*n^2 + n + 2

# program 2
def program2(L):
    squares = []
    for x in L:
        for y in L:
            if x == y:
                squares.append(x*y)
    return squares
# worst case : 4 * n^2 + n + 2

# program 3
def program3(L1, L2):
    intersection = []   1
    for elt in L1:  n 
        if elt in L2: n + 1
            intersection.append(elt)
    return intersection   1
# worst case : n ^ 2 + 2 * n + 2