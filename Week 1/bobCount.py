s = 'azcbobobegghakl'
def bobCount(string):
	bob = "bob"
	count = 0
	for char in range(len(string)):
		if string[char: char + 3 ] == bob:
			count += 1
	return count

def bobRgxCount(string):
	import re
	count = 0
	regex = r"([b][o][b])"
	li = re.findall(regex, string)
	print li
	for b in li:
		count += 1
	return count 
