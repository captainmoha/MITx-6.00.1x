# recursion on strings example 
#(Palindromes) : strings that read the same from both directions 

import string
s1 = 'abba'
s2 = 'able was I ere I saw elba'
s3 = 'nope'
s4 = 'Are we not drawn onward, we few, drawn onward to new era?'

def isPalindrome(s):
	# convert the string into lower case letters with no spaces
	def toChars(s):
		s = s.lower()
		ans = ''
		for c in s:
			if c in string.ascii_lowercase:
				ans += c
		return ans

	# actual is isPalindrome recursive function
	def isPal(s):
		# base case if the string is 1 letters or zero it's a palindrome
		if len(s) <= 1:
			return True

		else:
		# recursive steps
		# if the first and last letters are the same 
		#  then remove them and check the rest of the string again
		#  by calling the function isPal recursivly on the sliced string
		#  without the first and last charchters
			return (s[0] == s[-1]) and isPal(s[1:-1])
	# return the result of the input string after being converted to
	# lower case with no spaces and checked if it's a palindrome		
	return isPal(toChars(s))

print isPalindrome(s1)
print isPalindrome(s2)
print isPalindrome(s3)
print isPalindrome(s4)