balance = 999999
new_balance = balance
annualInterestRate = 0.18

# compute monthly interest rate
monthlyInterestRate = annualInterestRate / 12.0

month = 1
minMonthlyPayment = 0
# low bound to be the best case which is paying the whole debt throughout the year
low = new_balance / 12.0

# high bound is the worst case which is paying after the whole year + interest
high = (new_balance * (1 + monthlyInterestRate)**12)/12.0



while (abs(new_balance) >= 0.01):
    # reassigning new_balance in order to start the year loop again
    new_balance = balance

    # guess according to bisection search
    minMonthlyPayment = (low + high) / 2.0

    # reseting month
    month = 1

    # loop handle data of a year month by month 
    while (month <= 12 and new_balance > 0):
        # compute the balance after payment  
        new_balance -= minMonthlyPayment

        # get the interest for the current balance
        interest = monthlyInterestRate * new_balance

        # compute balance after adding the interest 
        new_balance += interest

        # infinite loop protection 
        month += 1


    # handling bisection
    if (new_balance < 0):
        # if the balance is negative then our guess was too high 
        # then we need to lower the guess by lowering the sum (low + high)
        # we do that by setting the higher bound to the first guess
        # the first guess is the middle of the interval from [low,high]
        # ie: the guess minMonthly payment = (low + high) / 2.0
        high = minMonthlyPayment
        pass

    elif (new_balance > 0):
        # if the balance is positive then our guess was too low 
        # then we need to increase the guess by increasing the sum (low + high)
        # we do that by setting the lower bound to the first guess
        # the first guess is the middle of the interval from [low,high]
        # ie: the guess minMonthly payment = (low + high) / 2.0
        low = minMonthlyPayment
        pass
    else:
        # if the new_balance = 0 
        # then we managed to find a good guess 
        # pass and get out of the loop hoooooooraaay
        pass
    
new_balance = round(new_balance, 2)
minMonthlyPayment = round(minMonthlyPayment, 2)
    

print ("Lowest Payment : " + str(minMonthlyPayment))