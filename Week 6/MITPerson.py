import datetime

class Person(object):
	def __init__(self, name):
		self.name = name
		self.birthday = None
		# two ways to get the last name 
		self.lastName = name.split(' ')[-1]
	        #lastBlank = self.name.rindex(' ') 
                #self.lastName = self.name[lastBlank + 1: ]
	def getLastName(self):
		return self.lastName
        
	def setBirthday(self, year, month, day):
		self.birthday = datetime.date(year, month, day)
            
	def getAge(self):
		if self.birthday == None:
			raise ValueError
		return (datetime.date.today() - self.birthday).days
        
	def __lt__(self, other):
		if self.lastName == other.lastName:
			return self.name < other.name
		return self.lastName < other.lastName
            
	def __str__(self):
		return self.name

class MITPerson(Person):
	nextIdNum = 0

	def __init__(self, name):
		# initialize person attributes
		Person.__init__(self, name) 
		self.idNum = MITPerson.nextIdNum
		MITPerson.nextIdNum += 1

	def getIdNum(self):
		return self.idNum
	# sorting in MITPerson uses id not name
	def __lt__(self, other):
		return self.idNum < other.idNum
