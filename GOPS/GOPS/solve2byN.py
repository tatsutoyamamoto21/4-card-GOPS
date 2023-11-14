import numpy as np
import itertools
from GOPS import solve2by2


def solve2byN(payout_a, payout_b, moves=False):
    c = payout_a[0, 0] + payout_b[0, 0]
    cols = np.array([z for z in range(payout_a.shape[1])])
    strategy_a = {}
    payoffs_b = {}

    combs = list(itertools.combinations(cols, 2))

    for i in combs:
        nash = np.array(i)
        check = np.setdiff1d(cols, nash)

        result = solve2by2(payout_a[:, nash], payout_b[:, nash], moves=True)
        
        for j in check:
            if sum(result[1][0]) > 1:
                test = min(payout_b[:, j])
                    
            else:
                test = np.matmul(result[1][0], payout_b[:, j])
            

            if result[0][1] >= test:
                strategy = np.zeros(payout_a.shape[1])
                ind = 0
                for k in nash:
                    strategy[k] = result[1][1][ind]
                    ind += 1

                strategy_a[tuple(strategy)] = result[1][0]
                payoffs_b[tuple(strategy)] = result[0][1]


    max_payoff_b = max(payoffs_b.values())
    max_strategy = []

    for key, val in payoffs_b.items():
        if val == max_payoff_b:
            max_strategy.append(key)

    if len(max_strategy) > 1:
        index = [sum(k) for k in max_strategy]
        l = 0
        for ind in index:
            if ind == max(index):
                max_strategy = max_strategy[l]
                break
            l += 1
    else:
        max_strategy = max_strategy[0]
    if moves:
        return (c-max_payoff_b, max_payoff_b), (strategy_a[max_strategy], list(max_strategy))
    return (c-max_payoff_b, max_payoff_b)