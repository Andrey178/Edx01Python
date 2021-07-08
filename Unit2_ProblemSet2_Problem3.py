balance = 5000  # the outstanding balance on the credit card
annualInterestRate = 0.18  # annual interest rate as a decimal
monthlyPaymentRate = 0.02  # minimum monthly payment rate as a decimal

balance = 320000
annualInterestRate = 0.2
#monthlyPaymentRate = 0.04


def month_payment(cur_balance, month_pay=monthlyPaymentRate * balance, annual_interest_rate=annualInterestRate):
    cur_balance_payment = month_pay
    cur_balance_interest = (cur_balance - cur_balance_payment) * annual_interest_rate / 12
    updated_balance = cur_balance - cur_balance_payment + cur_balance_interest

    return updated_balance, cur_balance_payment, cur_balance_interest


def fixed_month_payment(cur_balance, annual_interest_rate, months=12):
    month_interest_rate = annualInterestRate / 12
    month_payment_lower_bound = cur_balance / 12
    month_payment_upper_bound = (cur_balance * (1 + month_interest_rate) ** months) / months
    print(round(month_payment_lower_bound, 2), round(month_payment_upper_bound, 2))

    found_amount = False
    month_pay = month_payment_lower_bound + (month_payment_upper_bound - month_payment_lower_bound) / 2
    # month_pay = month_payment_lower_bound
    while not found_amount:
        end_balance = [cur_balance]
        for i in range(months):
            end_balance = month_payment(end_balance[0], month_pay, annual_interest_rate)

        if abs(end_balance[0]) <= 0.1:
            found_amount = True
        else:
            if end_balance[0] > 0:
                month_payment_lower_bound = month_pay
                month_pay = month_payment_lower_bound + (month_payment_upper_bound - month_payment_lower_bound) / 2
                # print(month_pay)
            else:
                month_payment_upper_bound = month_pay
                month_pay = month_payment_lower_bound + (month_payment_upper_bound - month_payment_lower_bound) / 2
            # month_pay += 0.01
    return round(month_pay, 2)


"""
        else:
            if cur_balance - end_balance[0] > 0:
                month_payment_lower_bound = month_pay
                month_pay = month_payment_lower_bound + (month_payment_upper_bound - month_payment_lower_bound) / 2
            else:
                month_payment_upper_bound = month_pay
                month_pay = month_payment_lower_bound + (month_payment_upper_bound - month_payment_lower_bound) / 2
"""



# cur_balance = [balance]
# for i in range(12):
#    cur_balance = month_payment(cur_balance[0])
#    print(cur_balance)
# print('Remaining Balance:', round(cur_balance[0], 2))
print('Lowest Payment:', fixed_month_payment(balance, annualInterestRate, months=12))

print("TEST!!!")
print('Lowest Payment 90325.03:', fixed_month_payment(999999, 0.18, months=12))
# print('Lowest Payment 440:', fixed_month_payment(4773, 0.2, months=12))
# print('Lowest Payment 360:', fixed_month_payment(3926, 0.2, months=12))
"""
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
"""



