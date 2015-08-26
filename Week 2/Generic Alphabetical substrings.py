s = 'azcbobobegghakl'
first_char = ''
second_char = ''
result1 = ''
len_result1 = len(result1)
end_result = ''
len_end_result = len(end_result)
dec_first_char = 0
dec_second_char = 0


for i in range(len(s) - 1):
    first_char = s[i]
    dec_first_char = ord(first_char)
    second_char = s[i+1]
    dec_second_char = ord(second_char)

    if (dec_second_char - dec_first_char) >= 0:
        result1 = first_char + second_char
        print result1
    


        
