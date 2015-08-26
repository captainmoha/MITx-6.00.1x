from ps4a import *
import time

#
#
# Problem #6: Computer chooses a word
#
#
def isValidWordComp(word, hand):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    wordLettersInHand = ''                     # empty string to fill with letter in hand
    copyHand = dict(hand)                      # copy of hand to iterate on
    
    for letter in word:
        if (letter in copyHand) and (copyHand[letter] != 0):  # conditions for a letter to be valid
            wordLettersInHand += str(letter)     # if the letter is valid add it to the new string
            copyHand[letter] -= 1                # subtract 1 from number of available similar letters

    if word == wordLettersInHand:                # if the letters in the match make up the word
        satisfiesHand = True
    else:
        satisfiesHand = False
    
    return satisfiesHand

def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxSoFar = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWordComp(word,hand):
            # Find out how much making that word is worth
            wordScore = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if wordScore > maxSoFar:
                # Update your best score, and best word accordingly
                maxSoFar = wordScore
                bestWord = word

    # return the best word you found.
    return bestWord

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    totalScore = 0
    handNew = dict(hand)
    # As long as there are still letters left in the hand:
    while calculateHandlen(handNew) > 0:
        
        # Display the hand
        print("Current Hand: "),
        displayHand(hand)
        # Ask user for input
        word = compChooseWord(hand, wordList, n)
        
        # If the computer has no more choices
        if compChooseWord == None:
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if isValidWord(word, hand, wordList) == False:
                # Reject invalid word (print a message followed by a blank line)
                print ("Invalid word, please try again.")
                print
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                totalScore += getWordScore(word, n)
                print ('"' + str(word) + '"' + " earned " + str(getWordScore(word, n)) + " points." + " Total: " + str(totalScore) + " points")
                print 
                # Update the hand 
                handNew = updateHand(handNew, word)
                if calculateHandlen(handNew) == 0 or len(word) == n or compChooseWord(handNew, wordList, n) == None:
                    break
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print("Total score: " + str(totalScore) + " points.")
   
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    n = HAND_SIZE
    firstCheck = False
    while True:
        usr = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if usr == 'n':
            while True:
                compOrMe = raw_input("Enter u to have yourself play, c to have the computer play: ")
                if compOrMe == 'u':
                    hand = dealHand(n)
                    playHand(hand, wordList,n)
                    firstCheck = True
                    break
                elif compOrMe == 'c':
                    hand = dealHand(n)
                    compPlayHand(hand, wordList, n)
                    firstCheck = True
                    break
                else:
                    print ("Invalid command.")

        elif usr == 'r':
            if firstCheck:
                while True:
                    compOrMe = raw_input("Enter u to have yourself play, c to have the computer play: ")
                    if compOrMe == 'u':
                        playHand(hand, wordList,n)
                        break
                    elif compOrMe == 'c':
                        compPlayHand(hand, wordList, n)
                        break
                    else:
                        print ("Invalid command.")    
            else:
                print ("You have not played a hand yet. Please play a new hand first!")
                
        elif usr == 'e':
            break
        else:
            print ("Invalid command.")

# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


