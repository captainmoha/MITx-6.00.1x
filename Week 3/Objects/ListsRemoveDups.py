
l1 = [1,2,3,4]
l2 = [1,2,5,6]
def removeDups(l1,l2):
    l1Start = l1[:]
    for i in l1Start:
	    if i in l2:
	        l1.remove(i)
    return l1
print removeDups(l1,l2)