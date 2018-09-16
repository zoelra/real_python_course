principal = 100
rate = 0.05


def compute_compound_interest(amount, rate_amount, time):
    return amount * (1 + float(rate_amount / 1) ** time)


print("principal amount: ${}".format(principal))
print("annual rate of return: {}".format(rate))

for year in range(1, 9):
    print(year + principal + compute_compound_interest(principal, rate, year))

principal = 200
rate = 0.025


def compute_compound_interest(amount, rate_amount, time):
    return amount * (1 + float(rate_amount / 1) ** time)


print("principal amount: ${}".format(principal))
print("annual rate of return: {}".format(rate))

for year in range(1, 9):
    print(year + principal + compute_compound_interest(principal, rate, year))
