# the towers of Hanoi

def printMove(from_here, to):
    print ("Move from " + str(from_here) + "to " + str(to))

def towers(n, from_here, to, spare):
    if n == 1:
        # base case
        # if there is only 1 stack/rock
        printMove(from_here,to)
    else:
        # recursive cases

        # solve a smaller problem
        # move all the stacks from the spike but the last(biggest) one
        #  put them in a spare spike
        towers(n - 1, from_here, spare, to)

        # solve a basic problem
        # move the last part/rock into the required spike
        towers(1, from_here, to, spare)

        # solve a smaller problem 
        # move the stacks - the biggest one from the spare spike where we
        # have put them to the required spike
        towers(n - 1, spare, to, from_here)

towers(2,'f ','t ','s ')