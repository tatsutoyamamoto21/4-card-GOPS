import numpy as np
from GOPS import payout3by3


def payout4by4(c, a, b, moves=False):
    # c = [cards that appear in order]
    # a = [a cards]
    # b = [b cards]
    c_original = c.copy()
    a_original = a.copy()
    b_original = b.copy()
    c1, c2, c3, c4 = c[0], c[1], c[2], c[3]
    # initialize payout matrix
    payout_a = np.zeros((4,4))
    payout_b = np.zeros((4,4))
    # fill payout matrix
    for i, x in enumerate(a_original):
        for j, y in enumerate(b_original):
            if x > y:
                c.remove(c1)
                a.remove(x)
                b.remove(y)
                to_add = payout3by3(c,a,b)
                payout_a[i,j] += to_add[0] + c1
                payout_b[i,j] += to_add[1]
            if x == y:
                c.remove(c1)
                a.remove(x)
                b.remove(y)
                to_add = payout3by3(c,a,b)
                payout_a[i,j] += to_add[0] + (c1/2)
                payout_b[i,j] += to_add[1] + (c1/2)
            if x < y:
                c.remove(c1)
                a.remove(x)
                b.remove(y)
                to_add = payout3by3(c,a,b)
                ##print(to_add)
                payout_a[i,j] += to_add[0] 
                payout_b[i,j] += to_add[1] + c1
            c, a, b = c_original.copy(), a_original.copy(), b_original.copy()
    return payout_a, payout_b