# We can use the idea of bisection search to determine if a characte3r
# is in a string, so long as the string is sorted in alphabetical order.
# First, test the middle character of a string against the character 
# you're looking for (the "test character"). If they are the same,
# we are done - we've found the character we're looking for!
#If they're not the same, check if the test character is "smaller"
# than the middle character. If so, we need only consider the lower half
# of the string; otherwise, we only consider the upper half of the string. 

s1 = "Mohamed Ali Farouk"
smaller = 's1'
larger = ''
def isIn(char,aStr):
    # base cases
    # if the string is empty
    if len(aStr) == 0:
        return False
        pass
    # if the string has lengths is 1 char
    elif len(aStr) == 1: 
        if char == aStr:
            return True
        else:
            return False
    # if the the middle charchter is the string
    elif char == aStr[len(aStr) / 2]:
        return True

    # recursive stepts
    # if the charchter is farther out into the string 
    #  cut the first half and deal with the second only 
    elif char < aStr[len(aStr) / 2]:
        if char == aStr[len(aStr) / 2]:
            return True
        else:
            return isIn(char, aStr[:len(aStr)/2])

    # if the charchter is closer to the begining of the string 
    #  cut the second half and deal with the first only
    elif char > aStr[len(aStr)/2]:
        if char == aStr[len(aStr) / 2]:
            return True
        else:
            return isIn (char, aStr[(len(aStr )/2):])
    else:
        return False
        
print isIn('c', 'cdirvx')
print isIn('b', 'bdnovz')
print isIn('p', s1)
print isIn('s', smaller)
print isIn('', larger)


