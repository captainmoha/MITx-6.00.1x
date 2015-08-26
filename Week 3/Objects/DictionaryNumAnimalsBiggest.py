animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd':['donkey', 'dog', 'dingo']
}
def biggest(aDict):
    # count the number of elements in a value of type list 
    #  in the dictionary
    count = 0
    # place holder for the biggest length in a value so far
    big = 0
    # key of the value which list has the biggest length
    k_big = 0
    # if the dictionary is empty
    if len(aDict) == 0:
        return None
    # loop on the elements of the dictionary (the keys)    
    for i in aDict.keys():
        # if length of the current value corresponding to the key
        #  is greater than 1 
        if (len(aDict[i]) > 1):
            # loop on elemnts of the list of the current value
            #  and count the elemnts
            #  keep the biggest value so far in 'big'
            for j in aDict[i]:
                count += 1
            if count >= big:
                big = count
                k_big = i
            # clean count for next iteration of the outer big loop
            count = 0
        # if the length of the list is 0 and k_big < 1
        #  ie no other lists are bigger than this one
        elif len(aDict[i]) == 0:
            if k_big < 1:
                # k_big is the current key in that case
                k_big = i
        else:
            pass
    # return the key which value has the longest list
    return k_big

# tests
print  biggest({}) # None
# result of the following should be 'a'
print  biggest({'a': [19, 0, 4, 18, 14, 7, 13, 6, 9], 'c': [2, 5], 'b': [9, 20, 18, 0], 'e': [4, 5, 14], 'd': [5, 20, 9, 16, 1, 20, 11]})