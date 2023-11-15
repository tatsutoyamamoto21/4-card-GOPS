import numpy as np
from GOPS import dominationfinal


def solve2by2(payout_a, payout_b, moves=False):
    if (payout_a[0] == payout_a[1]).all() and (payout_b[:, 0] == payout_b[:, 1]).all():
        result = (payout_a[0, 0], payout_b[0, 0])
        strategy = ([1,1],[1,1])
        if moves:
            return result, strategy
        return result

    A, B = np.ones((2,2)), np.ones((2,2))
    A[1,0], A[1,1] = payout_b[0,0]-payout_b[0,1], payout_b[1,0]-payout_b[1,1]
    B[1,0], B[1,1] = payout_a[0,0]-payout_a[1,0], payout_a[0,1]-payout_a[1,1]

    result = dominationfinal(payout_a, payout_b, moves)

    if result[0].shape != payout_a.shape:

        if moves:
            p_a, p_b = np.ones(2), np.ones(2)
            for i in result[2]:
                p_a[i] = 0
            for j in result[3]:
                p_b[j] = 0

            strategy = (list(p_a), list(p_b))
            return (result[0].sum() / max(result[0].shape), result[1].sum() / max(result[1].shape)), strategy
        else:
            return (result[0].sum() / max(result[0].shape), result[1].sum() / max(result[1].shape))

    else:
        p_a = np.linalg.solve(A, np.array([1, 0]))
        p_b = np.linalg.solve(B, np.array([1, 0]))

        for i, a in enumerate(p_a):
            if a < 0:
                p_a[i] = 0
                p_a = p_a/np.sum(p_a)
        
        for j, b in enumerate(p_b):
            if b < 0:
                p_b[j] = 0
                p_b = p_b/np.sum(p_b)
    
    
        result = (p_b[0] * payout_a[0, 0] + p_b[1] * payout_a[0, 1], p_a[0] * payout_b[0, 0] + p_a[1] * payout_b[1, 0])

        if moves:
            strategy = (list(p_a), list(p_b))
            return result, strategy
        else:
            return result
