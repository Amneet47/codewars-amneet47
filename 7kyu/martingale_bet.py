def martingale(bank, outcomes):
    if outcomes == []:
        return bank
    else:
        initial_bet = 100
        bet = initial_bet
        i = 0
        for i in outcomes:
            if i == 1:
                bank += bet
                bet = initial_bet
            elif i == 0:
                bank -= bet
                bet *= 2
    return bank

print(martingale(5100, [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0]))