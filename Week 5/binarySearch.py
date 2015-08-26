# binary search recursive

def search(L, e):
	# binary search function
	def bSearch(L, e, low, high):
		# base case this is the reason the recursion halts
		if high == low:
			return L[low] == e
		# mid point in the search space
		mid = low + int((high - low) / 2)

		# if the value of the mid point is greater than e
		# which is the target, I throw away the right part
		if L[mid] > e:
			return bSearch(L, e, low, mid -1)
		# otherwise throw away the left part
		else:
			return bSearch(L, e, mid + 1, high)

	# To get the party started
	# if the list is empty just return False
	if len(L) == 0:
		return False
	# otherwise call binarysearch with low being 0(first elem)
	# and high being the last element (len(L) - 1)
	else:
		return bSearch(L, e, 0, len(L) - 1)

#A recursive "Pythonic" binary search procedure:

def rBinarySearch(lista,element):
    if len(lista) == 1:
        return element == lista[0]
    mid = len(lista)/2
    if lista[mid] > element:
        return rBinarySearch( lista[ : mid] , element )
    if lista[mid] < element:
        return rBinarySearch( lista[mid : ] , element)
    return True


# binary search iterative
def search(L, e):
	# binary search function
    def bSearch(L, e, low, high):
        while low <= high:
            mid = low + int((high - low) / 2)
            if (L[mid] == e):
                return True
            elif (L[mid] > e):
                high = mid - 1
            else:
                low = mid + 1

	if low > high:
	    return False

    if len(L) == 0:
        return False
    else:
        return bSearch(L, e, 0, len(L) - 1)
print search(range(6), 9)

