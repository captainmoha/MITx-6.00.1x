#initial variables
balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04



def credit1(balance, annualinterestRate,monthlyPaymentRate):
    """ takes 3 numbers it is the main function to calculate the  minimum monthly payment 
    and the remaining balance as well as the total and the remaining in the end"""
    month = 1
    total = 0
    # loop to print data for every month 
    while (month <= 12):
        # compute the minumum amount to pay per month
        MinMonthlyPayment = (balance * monthlyPaymentRate)

        # compute the balance after payment  
        balance -= MinMonthlyPayment

        # compute monthly interest rate
        monthlyInterestRate = annualInterestRate / 12.0

        # get the interest for the current balance
        interest = monthlyInterestRate * balance
        # compute balance after adding the interest 
        balance += interest

        # keep the total in mind for printing later 
        total += MinMonthlyPayment

        # print the results
        print ("Month: " + str(month))
        print ("Minimum monthly payment: " + str(round(MinMonthlyPayment, 2)))
        print ("Remaining balance: " + str(round(balance, 2)))

        # infinite loop protection 
        month += 1

        print
        pass
    
    #print the total and the remaining balance     
    print ("Total Paid: " + str(round(total,2)))
    print ("Remaining balance: " + str(round(balance,2)))


