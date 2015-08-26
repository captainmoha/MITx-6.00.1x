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
        return self.value


# creating the binaryTree
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
