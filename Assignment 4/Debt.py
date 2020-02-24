def lend_money(debts, person, amount):
    if person not in debts:
        debts[person] = [amount]
    elif person in debts:
        debts[person].append(amount)
    return None


def amount_owed_by(debts, person):
    owed = 0
    if person not in debts:
        return 0
    else:
        for i in range(0, len(debts[person])):
            owed += debts[person][i]
    return owed


def total_amount_owed(debts):
    total = 0
    for i in debts:
        for j in range(0, len(debts[i])):
            if len(debts) == 0:
                break
            else:
                total += debts[i][j]
    return total
