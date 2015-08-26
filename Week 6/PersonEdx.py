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
