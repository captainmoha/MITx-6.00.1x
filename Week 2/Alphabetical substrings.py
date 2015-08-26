s = 'azcbobobegghakl'
result1 = s[0]
end_result = s[0]
end_len = 0

for i in range(len(s) - 1):
	if (s[i + 1] >= s[i]):
		result1 += s[i + 1]

		if (len(result1) > end_len):
			end_len = len(result1)
			end_result = result1 
	else:
		result1 = s[i + 1]
print end_result