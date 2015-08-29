import regex as re
s = 'azcbobobegghakl'
def bobCount(string):
	bob = "bob"
	count = 0
	for char in range(len(string)):
		if string[char: char + 3 ] == bob:
			count += 1
	return count


