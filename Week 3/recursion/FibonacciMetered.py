# febonacci metered
# global variables 
x = 0

def fibMetered(n):
    global numCalls
    numCalls += 1
    if n == 0 or n == 1:
        return 1
    else:
        return fibMetered(n-1) + fibMetered(n-2)

def testFib(n):
    for i in range(n + 1):
        global numCalls
        numCalls = 0
        print ("Fibonacci of " + str(i) + " = " + str(fibMetered(i)))
        print ("Fibonacci called " + str(numCalls) + " times")
        print
testFib(20)