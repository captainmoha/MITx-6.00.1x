from MITPerson import *

class Student(MITPerson):
	pass
class underGrad(Student):

	def __init__(self, name, classYear):
		MITPerson.__init__(self, name)
		self.year = classYear
	def getClass(self):
		return self.year

class grad(Student):
	pass

def isStudent(obj):
	return isinstance(obj, Student)


