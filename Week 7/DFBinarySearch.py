# binary tree class
class binaryTree(object):
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.leftBranch = None
        self.rightBranch = None

    # setting methods
    def setLeftBranch(self, node):
        self.leftBranch = node
    def setRightBranch(self, node):
        self.rightBranch = node
    def setParent(self, parent):
        self.parent = parent

    # getting methods
    def getValue(self):
        return self.value
    def getLeftBranch(self):
        return self.leftBranch
    def getRightBranch(self):
        return self.rightBranch
    def getParent(self):
        return self.parent

    def __str__(self):
        return self.valu
# target reached checkin function targetReached(target, startNode)
# startingNode is an object
def targetReached(startingNode, target):
    return startingNode.getValue() == target

# function to trace the path of search used in enhanced versions
def tracePath(node):
    # if the node has no parents return a list of it 
    if not node.getParent(): # base case
        return [node]
    # if the node has parents then recursively get them
    #  and return a list of nodes
    else:
        return [node] + tracePath(node.getParent()) # recursive step

# function to get the values of nodes returned by tracePath()
def getPathValues(nodesList):
    nodes = []
    for node in nodesList:
        nodes.insert(0,node.getValue())
    return nodes

# first Depth first search (DFS). uses a stack last in first out(LIFO)
def DFSBinary(root, targetReached, target):
    # create the stack
    stack = [root] 
    # while the stack is not empty
    while len(stack) > 0:
        # pring current node
        print "At node ", stack[0].getValue()
        # if target is found you're golden
        if targetReached(stack[0], target):
            return True

        # if not
        else:
            # pop the first element and keep it in a temp to check if it has branches
            temp = stack.pop(0)
            # check if the node has branches
            # if so insert them into the stack in order from left to right
            if temp.getRightBranch():
                stack.insert(0, temp.getRightBranch())
            if temp.getLeftBranch():
                stack.insert(0, temp.getLeftBranch())

    # if the value is not found just return False
    return False

# This one traces nodes traversed
def DFSBinaryTrace(root, targetReached, target):
    # create the stack
    stack = [root] 
    # while the stack is not empty
    while len(stack) > 0:
        # if target is found you're golden
        if targetReached(stack[0], target):
            return getPathValues(tracePath(stack[0]))

        # if not
        else:
            # pop the first element and keep it in a temp to check if it has branches
            temp = stack.pop(0)
            # check if the node has branches
            # if so insert them into the stack in order from left to right
            if temp.getRightBranch():
                stack.insert(0, temp.getRightBranch())
            if temp.getLeftBranch():
                stack.insert(0, temp.getLeftBranch())

    # if the value is not found just return False
    return False


# creating the binary Tree
# intializing instances
n5 = binaryTree(5) # root parent of n2(left) and n8(right)

# left branch n2 child of root parent of n1 and n4
n2 = binaryTree(2) # child of root and parent of its branches n1 and n4
n1 = binaryTree(1) # child of n2
n4 = binaryTree(4) # child of n2 and parent of n3
n3 = binaryTree(3) # child of n4

# right branch n8 child of root parent of n6
n8 = binaryTree(8) # child of root and parent of its branch 6
n6 = binaryTree(6) # child of n8 and parent of n7
n7 = binaryTree(7) # child of n6

# let's create relations based on the comments 
# starting from root
n5.setLeftBranch(n2)
n5.setRightBranch(n8)

# left branch n2 child of root parent of n1 and n4
n2.setParent(n5)
n2.setLeftBranch(n1)
n1.setParent(n2)
n2.setRightBranch(n4)
n4.setParent(n2)
n4.setLeftBranch(n3)
n3.setParent(n4)

# right branch n8 child of root parent of n6
n8.setParent(n5)
n8.setLeftBranch(n6)
n6.setParent(n8)
n6.setRightBranch(n7)
n7.setParent(n6)
