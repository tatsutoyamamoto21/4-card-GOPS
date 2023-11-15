import numpy as np
from GOPS import payout2by2, solve3by3


def payout3by3(c, a, b, moves=False):
    # c = [cards that appear in order]
    # a = [a cards]
    # b = [b cards]
    c_original = c.copy()
    a_original = a.copy()
    b_original = b.copy()
    ##print(c)
    c1, c2, c3 = c[0], c[1], c[2]
    c_a, c_b = c.copy(), c.copy()
    # initialize payout matrix
    payout_a = np.zeros((3,3))
    payout_b = np.zeros((3,3))
    # fill payout matrix
    for i, x in enumerate(a_original):
        for j, y in enumerate(b_original):
            if x > y:
                #print(c, c1, x, y)
                c_a.remove(c1)
                c_b.remove(c1)
                a.remove(x)
                b.remove(y)
                
                payout_a[i,j] += payout2by2(c_a, a, b)[0] + c1
                payout_b[i,j] += payout2by2(c_b, a, b)[1]
            if x == y:
                #print(c, c1, x, y)
                c_a.remove(c1)
                c_b.remove(c1)
                a.remove(x)
                b.remove(y)

                payout_a[i,j] += payout2by2(c_a, a, b)[0] + (c1/2)
                payout_b[i,j] += payout2by2(c_b, a, b)[1] + (c1/2)
            if x < y:
                #print(c, c1, x, y)
                c_a.remove(c1)
                c_b.remove(c1)
                a.remove(x)
                b.remove(y)
                
                payout_a[i,j] += payout2by2(c_a, a, b)[0] 
                payout_b[i,j] += payout2by2(c_b, a, b)[1] + c1
            c_a, c_b, a, b = c_original.copy(), c_original.copy(), a_original.copy(), b_original.copy()
    return solve3by3(payout_a, payout_b, moves)
