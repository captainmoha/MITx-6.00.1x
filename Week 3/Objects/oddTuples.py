# return only odd tuple elements as a tuple

def oddTuples(aTup):
	tup = ()
	for i in range(len(aTup)):
		if (i % 2 == 0):
			tup += (aTup[i],)
	return tup

print oddTuples(('I', 'am', 'a', 'test', 'tuple'))