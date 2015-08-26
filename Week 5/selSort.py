# selection sort 

def selSort(L):
	# go through the list
	for i in range(len(L)-1):
		# current index and value
		minIndex = i 
		minVal = L[i]
		# next element
		j = i + 1
		# iterate over the list comparing current with next 
		while j < len(L):
			# if the current value is > the next one
			#  then the min should be that next value
			if minVal > L[j]:
				minIndex = j
				minVal = L[j]
			j += 1
		temp = L[i]
		L[i] = L[minIndex]
		L[minIndex] = temp

def newSort(L):
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1
