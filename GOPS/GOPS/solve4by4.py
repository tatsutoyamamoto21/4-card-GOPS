import numpy as np
from GOPS import solve2by2, solve2byN, solve3by3, dominationfinal


def solve4by4(payout_a, payout_b, moves=False):
    # case when game is singular and irreducible
    if (payout_a[0] == payout_a[1]).all() and (payout_a[1] == payout_a[2]).all() and (payout_a[2] == payout_a[3]).all() and (payout_b[:,0] == payout_b[:,1]).all() and (payout_b[:,1] == payout_b[:,2]).all() and (payout_b[:,2] == payout_b[:,3]).all():
        result = (payout_a[0,0], payout_b[0,0])
        strategy = ([1,1,1,1], [1,1,1,1])
        if moves:
            return result, strategy
        else: 
            return result
    
    p_a, p_b = np.ones([2, 4])
    result = dominationfinal(payout_a, payout_b, moves)
    
    if result[0].shape == (1,1):
        ##print(result[0].shape)
        # take the singular equilibrium
        out_a = result[0][0]
        out_b = result[1][0]
        if moves:
            for i in result[2]:
                p_a[i] = 0
            for j in result[3]:
                p_b[j] = 0
            return (out_a, out_b), (p_a, p_b)
        return (out_a, out_b)

    elif result[0].shape == (1,2) or result[0].shape == (2,1):
        ##print(result[0].shape)
        # take highest value
        ret = (result[0].sum() / max(result[0].shape), result[1].sum() / max(result[1].shape))
        if moves:
            for i in result[2]:
                p_a[i] = 0
            for j in result[3]:
                p_b[j] = 0
            return ret, (p_a, p_b)
        return ret

    elif result[0].shape == (1,3) or result[0].shape == (1,3):
        ##print(result[0].shape)
        # take highest value
        ret = (result[0].sum() / max(result[0].shape), result[1].sum() / max(result[1].shape))
        if moves:
            for i in result[2]:
                p_a[i] = 0
            for j in result[3]:
                p_b[j] = 0
            return ret, (p_a, p_b)
        return ret

    elif result[0].shape == (2,2):
        ##print(result[0].shape)
        # use solve2by2
        if moves:
            ret, strat = solve2by2(result[0], result[1], moves)
            strat = list(strat)
            for i in result[2]:
                p_a[i] = 0
            for j in result[3]:
                p_b[j] = 0
            for i, a in enumerate(p_a):
                if a != 0:
                    p_a[i] = strat[0][0]
                    strat[0].remove(strat[0][0])
            for j, b in enumerate(p_b):
                if b != 0:
                    p_b[j] = strat[1][0]
                    strat[1].remove(strat[1][0])
            return ret, (p_a, p_b)
        
        return solve2by2(result[0], result[1], moves)
    
    elif result[0].shape == (2,3):
        ##print(result[0].shape)
        # use solve2byN
        if moves:
            ret, strat = solve2byN(result[0], result[1], moves)
            strat = list(strat)
            for i in result[2]:
                p_a[i] = 0
            for j in result[3]:
                p_b[j] = 0
            for i, a in enumerate(p_a):
                if a != 0:
                    p_a[i] = strat[0][0]
                    strat[0].remove(strat[0][0])
            for j, b in enumerate(p_b):
                if b != 0:
                    p_b[j] = strat[1][0]
                    strat[1].remove(strat[1][0])
            return ret, (p_a, p_b)
        
        return solve2byN(result[0], result[1], moves)

    elif result[0].shape == (3,2):
        ##print(result[0].shape)
        # use solve 2byN
        b = solve2byN(result[1].T, result[0].T, moves)[0]
        a = solve2byN(result[1].T, result[0].T, moves)[1]
        p_b = solve2byN(result[1].T, result[0].T, moves=True)[1][0]
        p_a = solve2byN(result[1].T, result[0].T, moves=True)[1][1]
        if moves:
            strat_a, strat_b = np.ones(4)
            for i in result[2]:
                strat_a[i] = 0
            for j in result[3]:
                strat_b[j] = 0
            for i, a in enumerate(strat_a):
                if a != 0:
                    strat_a[i] = p_a[0]
                    p_a.remove(p_a[0])
            for j, b in enumerate(strat_b):
                if b != 0:
                    strat_b[j] = p_b[0]
                    p_b.remove(p_b[0])
            return (a, b), (strat_a, strat_b) 
        
        return (a, b)
    
    elif result[0].shape == (3,3):
        # use solve 3by3
        if moves:
            ret, strat = solve3by3(result[0], result[1], moves)
            strat = list(strat)
            print(solve3by3(result[0], result[1], moves))
            print(strat)
            print(result)
            for i in result[2]:
                p_a[i] = 0
            for j in result[3]:
                p_b[j] = 0
            for i, a in enumerate(p_a):
                if a != 0:
                    p_a[i] = strat[0][0]
                    strat[0] = np.delete(strat[0], 0)

            for j, b in enumerate(p_b):
                if b != 0:
                    p_b[j] = strat[1][0]
                    strat[1] = np.delete(strat[1], 0)
            return ret, (p_a, p_b)
        
        return solve3by3(result[0], result[1], moves)
    
    else:
        ##print(result[0].shape)
        # solve the system of equations
        A, B = np.ones((4,4)), np.ones((4,4))
        A[1,0], A[1,1], A[1,2], A[1,3] = payout_b[0,0]-payout_b[0,1], payout_b[1,0]-payout_b[1,1], payout_b[2,0]-payout_b[2,1], payout_b[3,0]-payout_b[3,1]
        A[2,0], A[2,1], A[2,2], A[2,3] = payout_b[0,0]-payout_b[0,2], payout_b[1,0]-payout_b[1,2], payout_b[2,0]-payout_b[2,2], payout_b[3,0]-payout_b[3,2]
        A[3,0], A[3,1], A[3,2], A[3,3] = payout_b[0,0]-payout_b[0,3], payout_b[1,0]-payout_b[1,3], payout_b[2,0]-payout_b[2,3], payout_b[3,0]-payout_b[3,3]

        B[1,0], B[1,1], B[1,2], B[1,3] = payout_a[0,0]-payout_a[1,0], payout_a[0,1]-payout_a[1,1], payout_a[0,2]-payout_a[1,2], payout_a[0,3]-payout_a[1,3] 
        B[2,0], B[2,1], B[2,2], B[2,3] = payout_a[0,0]-payout_a[2,0], payout_a[0,1]-payout_a[2,1], payout_a[0,2]-payout_a[2,2], payout_a[0,3]-payout_a[2,3]
        B[3,0], B[3,1], B[3,2], B[3,3] = payout_a[0,0]-payout_a[3,0], payout_a[0,1]-payout_a[3,1], payout_a[0,2]-payout_a[3,2], payout_a[0,3]-payout_a[3,3]
        #print(payout_a)
        #print(payout_b)
        #print(A)
        #print(B)
        #print(result)
        p_a = np.linalg.solve(A, np.array([1, 0, 0, 0]))
        p_b = np.linalg.solve(B, np.array([1, 0, 0, 0]))
        print(p_a, p_b)

        for i, a in enumerate(p_a):
            if a < 0:
                p_a[i] = 0
                p_a = p_a/np.sum(p_a)
        
        for j, b in enumerate(p_b):
            if b < 0:
                p_b[j] = 0
                p_b = p_b/np.sum(p_b)
        
        ret = (p_b[0]*payout_a[0, 0] + p_b[1]*payout_a[0, 1] + p_b[2]*payout_a[0, 2] + p_b[3]*payout_a[0, 3], p_a[0]*payout_b[0, 0] + p_a[1]*payout_b[1, 0] + p_a[2]*payout_b[2, 0] + p_a[3]*payout_b[3, 0])

        if moves:
             return ret, (p_a, p_b)
        return ret