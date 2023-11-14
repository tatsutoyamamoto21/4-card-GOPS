import numpy as np
from GOPS import solve2by2


def payout2by2(c, a, b, moves=False):
    c1, c2 = c[0], c[1]
    
    payout_a = np.zeros((2,2))
    payout_b = np.zeros((2,2))
    
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x > y:
                payout_a[i,j] += c1
                payout_a[(i+1)%2,(j+1)%2] += c2
            elif x == y:
                payout_a[i,j] += c1/2
                payout_b[i,j] += c1/2
                payout_a[(i+1)%2,(j+1)%2] += c2/2
                payout_b[(i+1)%2, (j+1)%2] += c2/2
            else:
                payout_b[i,j] += c1
                payout_b[(i+1)%2,(j+1)%2] += c2
    
    #print(payout_a)
    #print(payout_b)
    
    return solve2by2(payout_a, payout_b, moves)