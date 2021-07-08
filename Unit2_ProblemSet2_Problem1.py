balance = 5000  # the outstanding balance on the credit card
annualInterestRate = 0.18  # annual interest rate as a decimal
monthlyPaymentRate = 0.02  # minimum monthly payment rate as a decimal

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


def month_payment(cur_balance):
    cur_balance_payment = cur_balance * monthlyPaymentRate
    cur_balance_interest = (cur_balance - cur_balance_payment) * annualInterestRate / 12
    updated_balance = cur_balance - cur_balance_payment + cur_balance_interest

    return updated_balance, cur_balance_payment, cur_balance_interest


cur_balance = [balance]
for i in range(12):
    cur_balance = month_payment(cur_balance[0])
#    print(cur_balance)
print('Remaining Balance:', round(cur_balance[0], 2))
