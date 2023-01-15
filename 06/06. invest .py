def invest(amount, rate, years):
    """ Deposit calculations. Arguments are: amount, rate, years """
    i = 1
    while(i <= years):
        amount += amount * rate
        print(f"Year {i}: ${amount:.2f}")
        i += 1

invest(100, 0.05, 4)