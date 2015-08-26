class Queue(object):
	def __init__(self):
		self.que = []
		pass
	def insert(self, e):
		self.que.insert(0,e)
		pass
	def remove(self):
		try:
			x = self.que.pop()
			return x
		except:
			raise ValueError("Queue already empty!")
		pass
	def __str__(self):
		return "[" + ",".join([str(e) for e in self.que]) + "]"
	def __len__(self):
		return len(self.que)