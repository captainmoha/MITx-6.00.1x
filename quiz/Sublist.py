aList = ["apple", "cat", "dog", "banana"]
# function to return only the strings which lengths are < 4
# the output should be a list of those strings
def lessThan4(aList):
	# empty string for use as a bag
    res_list = []
    # loop through the items of the list (strings)
    for i in aList:
    	# if the string is less than 4 chars long append to the list
	    if len(i) < 4:
		    res_list.append(i)
	# return the list after you get out of the loop		
    return res_list		
# test
print lessThan4(aList)