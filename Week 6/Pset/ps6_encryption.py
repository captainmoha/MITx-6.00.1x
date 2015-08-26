# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "C:/Users/Moha/Desktop/Spass/Python/6.00.1x Files/Week 6/Pset/words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("C:/Users/Moha/Desktop/Spass/Python/6.00.1x Files/Week 6/Pset/story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    cipherDict = {}
    LOWERCASE = string.ascii_lowercase
    UPPERCASE = string.ascii_uppercase
    plainList = list(UPPERCASE + LOWERCASE)

    for letter in plainList:
        # value is the result of a shifted letter, modulo used to "wrap around" the list
        value = plainList[(plainList.index(letter) + shift ) % len(plainList)]
        if letter in LOWERCASE:
            value = value.lower()
        elif letter in UPPERCASE:
            value = value.upper()
        cipherDict[letter] = value

    return cipherDict

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    resString = ''
    for letter in text:
        if letter in coder:
            resString += coder[letter]
        else:
            resString += letter 
    return resString

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### HINT: This is a wrapper function.

    return applyCoder(text, buildCoder(shift))

#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """

    # 1. init bestShift = 0, bestVIR(Best valid to invalid words ratio) = 0
    bestShift = 0
    bestVIR = 0
    # 2. create a list of words from text
    wordsInText = text.split(" ") 
    # 3. enter a for loop over all possible shifts range(26)
    for shift in range(26):
        newText = applyShift(text, shift)
        wordsInText = newText.split(" ")
        # 3.1 init numValidWords = 0, VIR(valid to invalid words ratio) = 0
        numValidWords = 0
        VIR = 0
        # 3.2 enter a for loop over words in the created list from text
        for word in wordsInText:
            # 3.2.1 if the word is valid ie: isWord() returns True
            if isWord(wordList, word):
                # 3.2.1.1 increment numValidWords
                numValidWords += 1
        # 3.3 compute VIR = numValidWords / len(created list from text)
        #print "valid words", numValidWords
        #print "len(wordsInText)", len(wordsInText)
        VIR = numValidWords % len(wordsInText)
        #print "VIR ", VIR
        # 3.4 if VIR = 1 ie all words are valid 
        if numValidWords == len(wordsInText):
            # 3.4.1 return current shift ie : best shift
            return shift
        # 3.5 else if VIR >= bestVIR
        elif VIR >= bestVIR:
            # 3.5.1 bestVIR = VIR
            bestVIR = VIR
            # 3.5.2 bestshift = shift
            bestShift = shift
    # 4. return bestShift
    if bestVIR == 0:
        return 0
    else:
        return bestShift

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    ### TODO.
    story = getStoryString()
    #print story
    wordList = loadWords()
    shift = findBestShift(wordList, story)
    #print shift
    return applyShift(story, shift)

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    wordList = loadWords()
    s = applyShift('Hello, world!', 8)
    bestShift = findBestShift(wordList, s)
    assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
    #    decryptStory()
