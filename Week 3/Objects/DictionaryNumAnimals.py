# find the number of animals in the dictionary
x = {'a': [2, 2, 5, 0, 3], 'e': [], 'D': [0, 12], 'F': [], 'j': [], 'N': [], 'r': [7, 17, 18], 't': [5, 20, 2, 11, 0], 'W': [15, 8, 8, 10, 13], 'X': []}
# ans is 20

def howMany(aDict):
    count = 0
    for i in aDict.values():
        if len(i) > 1:
            for j in i:
                count += 1
        elif len(i) == 1:
            count += 1
        else:
            pass
    return count 
print howMany(x)