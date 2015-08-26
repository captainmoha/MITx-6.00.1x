# Write a Python function that returns a list of keys in aDict with
#  the value target. The list of keys you return should be sorted
#  in increasing order. The keys and values in aDict are both integers.
#  (If aDict does not contain the value target,
#   you should return an empty list.)

# This function takes in a dictionary and an integer and returns
#  a list.

d = {1:3, 2:8, 3:9, 4:5, 5:9}
tar = 9
res_list = []
def keysWithValue(aDict,target):
    res_list = []
    for i in aDict.keys():
        if aDict[i] == target:
            res_list.append(i)
    return res_list

