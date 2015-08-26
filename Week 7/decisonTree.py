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
        return self.value

        
def buildDTree(sofar, todo):
	"""
	Building the decision tree recursively
	   input : sofar list of things I have included so far
	   		 : todo list of things I still have to decide about
	   output: decision tree 
	"""
	
	if (len(todo) == 0):                  # if there is nothing in the todo list
		return binaryTree(sofar)          # create a tree of the list sofar (base case)

	else:												   # if there are elements in todo list
		withElt = buildDTree(sofar + todo[0], todo[1:])    # first decision to include the first
		withoutElt = buildDTree(sofar, todo[1:])		   # second decision to exclude the first
		hereNode = binaryTree(sofar)				       # create node
		hereNode.setLeftBranch(withElt)					   # set leftbranch
		hereNode.setRightBranch(withoutElt)
		return hereNode
# target reached checkin function targetReached(target, startNode)
# startingNode is an object
def targetReached(startingNode, target):
    return startingNode.getValue() == target

def constraintFcn(nodeVal):

	pass
def DFSDecisionTree(root, targetReached, constraintFcn, target):
	"""
	searching a decision tree depth first
	"""
	stack = [root]
	best = None
	visited = 0

	while (len(stack) > 0):
		visited += 1
		if constraintFcn(stack[0].getValue()):
			if best == None:
				best = stack[0]
			elif targetReached(stack[0], target) > targetReached(best, target):
				best = stack[0]

			temp = stack.pop(0)
			if temp.getRightBranch():
				stack.insert(0, temp.getRightBranch())
			if temp.getLeftBranch():
				stack.insert(0, temp.getLeftBranch())
		else:
			stack.pop(0)
	print "visited", visited
	return best

def BFSDecisionTree(root, targetReached, constraintFcn, target):
	"""
	searching a decision tree breadth first
	"""
	queue = [root]
	best = None
	visited = 0

	while (len(queue) > 0):
		visited += 1

		if constraintFcn(queue[0].getValue()):
			if best == None:
				best = queue[0]
			elif targetReached(queue[0],target) > targetReached(best, target):
				best = queue[0]

			temp = queue.pop(0)

			if temp.getLeftBranch():
				queue.append(temp.getLeftBranch)
			if temp.getRightBranch():
				queue.append(temp.getRightBranch)
		else:
			queue.pop(0)
	print "visited", visited
	return best