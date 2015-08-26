class intSet(object):

	def __init__(self):
		self.vals = []
	def insert(self, e):
		if not e in self.vals:
			self.vals.append(e)
	def __str__(self):
		self.vals.sort()
		return "{" + ','.join([str(e) for e in self.vals]) + "}"
	def member(self, e):
	        return e in self.vals
	def remove(self, e):
	   try:
		  self.vals.remove(e)
	   except:
		  raise ValueError(str(e) + " Not found!")
	def intersect(self, other):
	    interset = []
	    for e in self.vals:
	        for d in other.vals:
	            if e == d:
	                interset.append(e)
	    return "{" + ','.join([str(e) for e in interset]) + "}" 
	def __len__(self):
		return len(self.varl)