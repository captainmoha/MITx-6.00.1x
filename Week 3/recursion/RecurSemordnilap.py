# A semordnilap is a word or a phrase that spells a different word 
# when backwards ("semordnilap" is a semordnilap of "palindromes").
# Here are some examples:
s1 = 'nametag'
s2 = 'gateman'

s3 = 'dog'
s4 = 'god'
s5 = 'live'
s6 = 'eril'
s7 = 'desserts'
s8 = 'stressed'
# Wrapper function for stuff that we should only check once at first
def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)

# actual semordnilap function 
def semordnilap(str1, str2):
    # base cases
    # if the lengths is different 
    if len(str1) != len(str2):
        return False
    # if the length is 1 for both of the strings 
    elif len(str1) == 1 and len(str2) ==1:
        if str1 == str2:
            return True
        else:
            return False  

    # recursive cases
    # if the first letter in str1 == the last letter in str2
    # recall the function with new parameters which are
    # the first string after slicing the first letter
    # the second string after slicing the last letter     
    else: 
        if str1[0] == str2[len(str2)-1]:
            return semordnilap(str1[1:len(str1)],str2[0:len(str2)-1])
        else: 
            return False
 # tests        
print semordnilapWrapper(s1,s2)
print semordnilapWrapper(s3,s4)
print semordnilapWrapper(s5,s6)
print semordnilapWrapper(s7,s8)