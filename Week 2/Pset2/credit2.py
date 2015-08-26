balance = 3329
new_balance = balance
annualInterestRate = 0.2
month = 1
minMonthlyPayment = 0

# loop to print data for every month 
while (new_balance > 0):
    new_balance = balance
    minMonthlyPayment += 10
    month = 1
    while (month <= 12 and new_balance > 0):
        # compute the balance after payment  
        new_balance -= minMonthlyPayment

        # compute monthly interest rate
        monthlyInterestRate = annualInterestRate / 12.0

        # get the interest for the current balance
        interest = monthlyInterestRate * new_balance
        # compute balance after adding the interest 
        new_balance += interest

        # infinite loop protection 
        month += 1

    new_balance = round(new_balance,2)
    

print ("Lowest Payment : " + str(minMonthlyPayment))