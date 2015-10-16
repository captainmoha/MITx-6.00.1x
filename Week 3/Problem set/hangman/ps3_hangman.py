# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    matches = 0

    for letter in secretWord:
        if letter in lettersGuessed:
            matches += 1
    if matches == len(secretWord):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    output = ""
    UNDER_SCORE = "_"
    for letter in secretWord:
        if letter in lettersGuessed:
            output += letter
        else:
            output += UNDER_SCORE
    return output



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    LOWER_CASE = string.ascii_lowercase
    output = ""
    for letter in LOWER_CASE:
        if letter not in lettersGuessed:
            output += letter
    return output

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    numGuesses = 8
    lenWord = len(secretWord)
    lettersGuessed = []

    print "Welcome to the game Hangman!"
    print "I am thinking of a word that is %d letters long" % lenWord

    while (numGuesses > 0) and (not isWordGuessed(secretWord, lettersGuessed)):
        print "-----------"
        print "You have %d guesses left" % numGuesses
        print "Available Letters: %s" % getAvailableLetters(lettersGuessed)

        usr_input = raw_input("Please guess a letter: ")
        usr_input = usr_input.lower()

        if (usr_input in secretWord) and (usr_input not in lettersGuessed):
            lettersGuessed.append(usr_input)
            if isWordGuessed(secretWord, lettersGuessed):
                print "Good guess:", getGuessedWord(secretWord, lettersGuessed)
                break
            else:
                print "Good guess:", getGuessedWord(secretWord, lettersGuessed)
        elif (usr_input in lettersGuessed):
            print "Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed)
        elif (usr_input not in secretWord):
            lettersGuessed.append(usr_input)
            print "Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed)
            numGuesses -= 1

    if isWordGuessed(secretWord, lettersGuessed):
        print "-----------"
        print "Congratulations, you won!"
    else:
        print "-----------"
        print "Sorry, you ran out of guesses. The word was %s." % secretWord 




secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
