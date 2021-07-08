balance = 5000  # the outstanding balance on the credit card
annualInterestRate = 0.18  # annual interest rate as a decimal
monthlyPaymentRate = 0.02  # minimum monthly payment rate as a decimal

balance = 356
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


def month_payment(cur_balance, month_pay=monthlyPaymentRate * balance, annual_interest_rate=annualInterestRate):
    cur_balance_payment = month_pay
    cur_balance_interest = (cur_balance - cur_balance_payment) * annual_interest_rate / 12
    updated_balance = cur_balance - cur_balance_payment + cur_balance_interest

    return updated_balance, cur_balance_payment, cur_balance_interest


def fixed_month_payment(cur_balance, annual_interest_rate, months=12):
    found_amount = False
    month_pay = 10
    while not found_amount:
        end_balance = [cur_balance]
        for i in range(months):
            end_balance = month_payment(end_balance[0], month_pay, annual_interest_rate)

        if end_balance[0] <= 0:
            found_amount = True
        else:
            month_pay += 10
    return month_pay



#cur_balance = [balance]
#for i in range(12):
#    cur_balance = month_payment(cur_balance[0])
#    print(cur_balance)
# print('Remaining Balance:', round(cur_balance[0], 2))
print('Lowest Payment:', fixed_month_payment(balance, annualInterestRate, months=12))

print("TEST!!!")
print('Lowest Payment 310:', fixed_month_payment(3329, 0.2, months=12))
print('Lowest Payment 440:', fixed_month_payment(4773, 0.2, months=12))
print('Lowest Payment 360:', fixed_month_payment(3926, 0.2, months=12))

print('Lowest Payment 30:', fixed_month_payment(325, 0.18, months=12))
print('Lowest Payment 40:', fixed_month_payment(423, 0.2, months=12))
print('Lowest Payment 40:', fixed_month_payment(356, 0.2, months=12))
print('Lowest Payment 80:', fixed_month_payment(873, 0.2, months=12))
print('Lowest Payment 430:', fixed_month_payment(4710, 0.18, months=12))
print('Lowest Payment 430:', fixed_month_payment(4612, 0.2, months=12))
print('Lowest Payment 410:', fixed_month_payment(4429, 0.18, months=12))
print('Lowest Payment 400:', fixed_month_payment(4629, 0.04, months=12))
print('Lowest Payment 310:', fixed_month_payment(3346, 0.18, months=12))
print('Lowest Payment 330:', fixed_month_payment(3648, 0.18, months=12))
print('Lowest Payment 380:', fixed_month_payment(4160, 0.15, months=12))
print('Lowest Payment 370:', fixed_month_payment(4053, 0.18, months=12))
print('Lowest Payment 40:', fixed_month_payment(326, 0.25, months=12))
print('Lowest Payment 360:', fixed_month_payment(4142, 0.04, months=12))
print('Lowest Payment 380:', fixed_month_payment(4201, 0.18, months=12))




