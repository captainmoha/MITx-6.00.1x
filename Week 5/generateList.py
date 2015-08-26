# generate a list of unsorted random integers
import random 

def generateList(length):
    unsortedList = []
    while length > 0:
        i = random.randrange(1,101)
        unsortedList.append(i)
        length -= 1
    return unsortedList
generateList(10)