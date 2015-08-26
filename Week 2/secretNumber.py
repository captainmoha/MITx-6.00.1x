low = 0
high = 100
isDone = False
#user_input = raw_input("Please think of a number between 0 and 100!")
guess = (high + low) / 2
# first output 
print "Please think of a number between 0 and 100!"

# handling input and making sure it's valid
while(isDone == False):
    print ("Is your secret number " + str(guess) + '?')
    user_input = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if (user_input == 'h'):
        high = guess  
    elif (user_input == 'l'  ):
        low = guess
    elif (user_input == 'c'):
        print ("Game over. Your secret number was: " + str(guess))
        isDone = True
        break
    else:
        print 'sorry I did not understand your input. Try again'
    guess = (high + low) / 2 
